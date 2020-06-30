from flask import g, Blueprint


bp = Blueprint("fifa_views", __name__)


@bp.route("/")
def testing_route():
    return "EUREKA"
