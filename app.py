from flask import Flask

# импортируем блюпринты из их пакетов
from main.views import main_blueprint
from loader.views import loader_blueprint

def main():
    app = Flask(__name__)

    #регистрируем блюпринт main
    app.register_blueprint(main_blueprint)
    #регистрируем блюпринт loader
    app.register_blueprint(loader_blueprint)

    app.run()
if __name__ == "__main__":
    main()
