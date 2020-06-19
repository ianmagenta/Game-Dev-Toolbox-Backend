from flask import Blueprint
from flask_cors import cross_origin
from ..auth import *
from app.models import db, User
import requests

bp = Blueprint("users", __name__, url_prefix='/users')


@bp.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response


@bp.route('', methods=['POST'])
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def user():
    data = request.json
    exists = User.query.filter_by(unique_id=data["sub"]).first()
    if exists:
        exists.unique_id = data["sub"]
        exists.name = data["nickname"]
        exists.email = data["email"]
        exists.picture = data["picture"]
    else:
        user = User(unique_id=data["sub"], name=data["nickname"],
                    email=data["email"], picture=data["picture"])
        db.session.add(user)
    db.session.commit()
    return '', 200


# # This doesn't need authentication

# @APP.route("/api/public")
# @cross_origin(headers=["Content-Type", "Authorization"])
# def public():
#     response = "Hello from a public endpoint! You don't need to be authenticated to see this."
#     return jsonify(message=response)


# # This needs authentication

# @APP.route("/api/private")
# @cross_origin(headers=["Content-Type", "Authorization"])
# @requires_auth
# def private():
#     response = "Hello from a private endpoint! You need to be authenticated to see this."
#     return jsonify(message=response)
