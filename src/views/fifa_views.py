from flask import g, Blueprint, request
from src.models import fifa_models

bp = Blueprint("fifa_views", __name__)


@bp.route("/", methods=["GET"])
def testing_route():
    return "EUREKA"


@bp.route("/test")
def test_route():
    if request.method == "POST":
        data = request.json()
        print(data)
    return "Test Worked"
