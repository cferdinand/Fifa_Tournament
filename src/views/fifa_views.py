from flask import g, Blueprint, request, render_template
from src.models import fifa_models as models

bp = Blueprint("fifa_views", __name__)


@bp.route("/", methods=["GET"])
def home_route():
    return render_template("index.html", flask_token="Hello World")


@bp.route("/tournament", methods=["GET", "POST", "PUT", "DELETE"])
def tournament_route():
    if request.method == "GET":
        data = request.args.get("name")
        res = models.get_tournaments(data)
        return {"tournament": res}
    elif request.method == "POST":
        data = request.json
        return {"tournament": models.add_tournament(data), "status": 201}
    elif request.method == "PUT":
        data = request.json

        new_tournament = models.update_tournamet(data)

        return {"tournament": new_tournament, "status": 204}


# @bp.route("/tournament/<string:id>", methods=["GET"])
# def userdata(id):
#     print(id)
#     return id

# @bp.route("/group",methods=["POST","PUT"])
# def create_group():
#     pass

# @bp.route()
