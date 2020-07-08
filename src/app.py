from flask import Flask
from .views import fifa_views as views


def create_app():
    app = Flask(__name__, instance_relative_config=True,
                static_folder="../frontend_react/public", template_folder="../frontend_react")
    app.register_blueprint(views.bp)

    return app


# if __name__ == "__main__":
#     app.run()
