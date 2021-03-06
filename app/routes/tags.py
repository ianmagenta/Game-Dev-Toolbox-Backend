from flask import Blueprint, jsonify
from flask_cors import cross_origin
from ..auth import *
from app.models import db, TaggedTool, User
import requests

bp = Blueprint("tags", __name__, url_prefix='/tags')


@bp.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response


@bp.route('user/<u_id>')
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def get_user_tags(u_id):
    user = User.query.filter_by(unique_id=u_id).first()
    if user:
        tags = TaggedTool.query.filter_by(
            user_id=user.id).order_by(TaggedTool.id)
        export = {i: v.to_dict() for i, v in enumerate(tags)}
        return export, 200
    else:
        return {}, 200


@bp.route('is_tagged', methods=["POST"])
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def get_tag():
    data = request.json
    user = User.query.filter_by(unique_id=data["id"]).first()
    if user:
        tag = TaggedTool.query.filter_by(
            user_id=user.id, tool_id=data["tool"]).first()
        if tag:
            return {"tagged": True}, 200
        else:
            return {"tagged": False}, 200
    else:
        return {"tagged": False}, 200


@bp.route('', methods=['POST'])
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def tag_post():
    data = request.json
    user = User.query.filter(User.unique_id == data["id"]).one()
    exists = TaggedTool.query.filter_by(
        user_id=user.id, tool_id=data["tool"]).first()
    if exists:
        db.session.delete(exists)
        db.session.commit()
        return {"tagged": False}, 200
    else:
        newTag = TaggedTool(user_id=user.id, tool_id=int(data["tool"]))
        db.session.add(newTag)
        db.session.commit()
        return {"tagged": True}, 200


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
