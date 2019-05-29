import logging

from flask import Blueprint, request

from models.user import User

from common.util.common_response import response

from app.user_app.serializers import (
    user_schema,
    users_schema,
    user_login_schema
)

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


user_api_blueprint = Blueprint(
    'user_api', __name__
)


@user_api_blueprint.route("/", methods=['GET', 'POST'], strict_slashes=False)
def users():
    """view for get users"""
    log.info("Users")
    # print(a)
    if request.method == "GET":
        users = users_schema.dump(User.query.all())
        return response(
            message="Data fetched successfully.",
            data=users.data,
            status=200
        )

    """View for Creating the user."""
    if request.method == 'POST':
        user_data = user_schema.load(request.get_json() or {})

        if user_data.errors:
            return response(
                message="Incorrect data were provided.",
                data={**user_data.errors},
                status=400
            )

        user = user_data.data
        user.save()
        user = user_schema.dump(user)
        return response(
            message="User created successfully.",
            data=user.data,
            status=201
        )
