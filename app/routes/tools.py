from flask import Blueprint, jsonify
from flask_cors import cross_origin
from ..auth import *
from app.models import db, Tool, AssociatedTool
import requests

bp = Blueprint("tools", __name__, url_prefix='/tools')


@bp.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response


@bp.route('/<tool_id>')
@cross_origin(headers=["Content-Type", "Authorization"])
def user(tool_id):
    tool = Tool.query.get(tool_id)
    if tool:
        tool_dict = tool.to_dict()
        tool_dict["associated"] = []
        associated = AssociatedTool.query.filter_by(primary_tool_id=tool_id)
        {tool_dict["associated"].append(i.to_dict()) for i in associated}
        return tool_dict, 200
    else:
        return {}, 200


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
