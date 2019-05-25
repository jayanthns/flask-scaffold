from flask import jsonify


def response(message, data=None, status=200):
    response_obj = {
        "message": message,
        "status": status
    }
    if data is not None:
        response_obj['data'] = data
    return jsonify(response_obj), status
