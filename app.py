from flask import Flask
import logging
# импортируем блюпринты из их пакетов
from main.views import main_blueprint
from loader.views import loader_blueprint


def main():
    # создание кастомного логгера с записью логов в файл log.txt
    new_logger = logging.getLogger('check_actions')
    new_logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler("log.txt", 'w')
    formatter_one = logging.Formatter("%(levelname)s : %(asctime)s : %(message)s")
    file_handler.setFormatter(formatter_one)
    new_logger.addHandler(file_handler)

    app = Flask(__name__)

    # регистрируем блюпринт main
    app.register_blueprint(main_blueprint)
    # регистрируем блюпринт loader
    app.register_blueprint(loader_blueprint)

    app.run()


if __name__ == "__main__":
    main()
