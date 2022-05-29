from flask import Flask, render_template, request, Blueprint
import utils
import logging

# создаем блюпринт и указываем источник шаблонов
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='..')
#подключаемся к логеру из app.py
new_logger = logging.getLogger('check_actions')


# создаем вьюшку главной станицы
@main_blueprint.route('/')
def general_page():
    return render_template("main/templates/index.html")


# создаем вьюшку страницы с постами
@main_blueprint.route('/search')
def posts_list_page():

    word_to_search = request.args.get('word_to_search')
    new_logger.info(f'Выполнен поиск по ключевому слову "{word_to_search}"')

    list_ = utils.load_data()
    if list_ != None:   #проверка возникновения ошибок при чтении файла json с постами
        finded_posts = utils.get_posts_by_word(list_, word_to_search)
        if finded_posts:    #ветвление в случае остутствия искомой информации среди всех постов
            return render_template('main/templates/posts_list.html', word_to_search=word_to_search, posts=finded_posts)
        return render_template("common_templates/error_page.html", error_name=f'Постов по запросу "{word_to_search}" не найдено!',
                               error_description='Попробуйте другое ключевое слово для поиска', page_back='/')
    return render_template("common_templates/error_page.html", error_name="Ошибка при загрузке файла posts.json",
                           error_description='Вероятно, файл отсутствует или его содержимое невозможно прочитать', page_back='/')

