from flask import Flask
from .views import fifa_views as views


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(views.bp)

    return app


# if __name__ == "__main__":
#     app.run()
