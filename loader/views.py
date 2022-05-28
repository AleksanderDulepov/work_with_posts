from flask import Flask, render_template, request, Blueprint, send_from_directory
import utils

# создаем блюпринт и указываем источник шаблонов
loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='..')


# создаем вьюшку формы добавления поста
@loader_blueprint.route('/adding')
def adding_post_page():
    return render_template("loader/templates/add_post.html")


# создаем вьюшку с результатами добавления поста
@loader_blueprint.route('/after_adding', methods=['POST'])
def after_adding_page():
    picture = request.files.get("picture_to_save")
    if not picture:  # проверка загрузки изображения
        return render_template("common_templates/error_page.html", error_name='Ошибка загрузки изображения',
                               error_description='Пожалуйста, проверьте загружаемый файл!', page_back='/adding')
    file_name = picture.filename
    if utils.check_format_file(file_name):  # проверка формата изображения
        picture_reference = f'./uploads/{file_name}'
        picture.save(picture_reference)
        description = request.form.get('description')

        if utils.add_post_to_json(picture_reference, description)!=False:
            list_ = utils.load_data()
            return render_template('loader/templates/after_adding.html', item=list_[-1])
        else:
            return render_template("common_templates/error_page.html", error_name='Ошибка при записи файла posts.json',
                                   error_description='С записью поста в файл произошла ошибка', page_back='/adding')

    return render_template("common_templates/error_page.html", error_name='Некорректный формат загрузки изображения',
                           error_description='Пожалуйста, загрузите изображение с расширением .jpg, .png', page_back='/adding')


@loader_blueprint.route('/uploads/<path:path>')
def make_static_dir(path):
    return send_from_directory('uploads', path)
