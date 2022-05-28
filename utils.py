import json
from config import POSTS_FILE
from Post_class import Post


# загрузка постов из файла
def load_posts_from_json(address):
    with open(address, 'r', encoding='UTF-8') as file:
        return json.load(file)


# создание обьектов класса POST и запаковка их в список
def get_objects_list(list_):
    objects_list = []
    for i in list_:
        objects_list.append(Post(i['pic'], i['content']))
    return objects_list


# загрузка файла постов и получение списка обьектов в однои блоке
def load_data():
    try:
        data_from_json = load_posts_from_json(POSTS_FILE)
        objects_list = get_objects_list(data_from_json)
        return objects_list
    except (json.JSONDecodeError, FileNotFoundError):
        return None


#добавление нового поста в json
def add_post_to_json(picture, description):
    try:
        previous_file = load_posts_from_json(POSTS_FILE)
        post_to_add = {'pic': picture, 'content': description}
        previous_file.append(post_to_add)
        with open(POSTS_FILE, 'w', encoding='utf-8') as file:
            json.dump(previous_file, file, ensure_ascii=False)
        return True
    except (json.JSONDecodeError, FileNotFoundError):
        return False

# список постов по ключевому слову
def get_posts_by_word(list_,word):
    output_list = []
    if word.strip() != '':
        for i in list_:
            if word.strip().lower() in i.description.lower():
                output_list.append(i)
        return output_list
    return list_


# проверка формата загружаемого файла
def check_format_file(filename):
    allowed_extensions = ['jpeg', 'png','jpg']
    if filename.split('.')[-1] in allowed_extensions:
        return True
    return False

