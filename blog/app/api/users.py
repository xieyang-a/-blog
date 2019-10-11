import re

from flask import request, jsonify, url_for

from app import db
from app.api import bp
from app.api.errors import bad_request
from app.models import User


@bp.route('/users',methods=['POST'])
def create_user():
    data = request.get_json()
    if not data:
        return bad_request('需提交数据')

    message = {}
    if 'username' not in data or not data.get('username',None):
        message['username'] = '需有效用户名.'
        pattern = '^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'
        if 'email' not in data or not re.match(pattern, data.get('email', None)):
            message['email'] = '需有效电子邮件.'
        if 'password' not in data or not data.get('password', None):
            message['password'] = '需有效密码.'

        if User.query.filter_by(username=data.get('username', None)).first():
            message['username'] = '用户名已存在.'
        if User.query.filter_by(email=data.get('email', None)).first():
            message['email'] = '已存在同名电子邮件.'
        if message:
            return bad_request(message)

        user = User()
        user.from_dict(data, new_user=True)
        db.session.add(user)
        db.session.commit()
        response = jsonify(user.to_dict())
        response.status_code = 201
        # HTTP协议要求201响应包含一个值为新资源URL的Location头部
        response.headers['Location'] = url_for('api.get_user', id=user.id)
        return response


@bp.route('/users',methods=['GET'])
def get_users():
    pass

@bp.route('/users/<int:id>',methods=['GET'])
def get_user(id):
    return jsonify(User.query.get_or_404(id).to_dict())

@bp.route('/users/<int:id>',methods=['PUT'])
def update_user(id):
    pass

@bp.route('/users/<int:id>',methods=['DELETE'])
def delete_user(id):
    pass

