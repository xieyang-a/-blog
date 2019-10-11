from flask import jsonify

from app.api import bp

@bp.route('/ping')
def ping():
    return jsonify('ping!')
