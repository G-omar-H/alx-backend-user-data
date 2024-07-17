#!/usr/bin/env python3
"""
session_auth.py
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_auth():
    """
    session authtentification mechanism
    """
    sessionName = os.getenv('SESSION_NAME')
    emailCredential = request.form.get('email')
    passwordCredential = request.form.get('password')
    if not emailCredential or emailCredential == '':
        return jsonify({"error": "email missing"}), 400
    if not passwordCredential or passwordCredential == '':
        return jsonify({"error": "password missing"}), 400
    users = User.search({'email': emailCredential})
    if not users or users == {}:
        return jsonify({"error": "no user found for this email"}), 404
    for user in users:
        if user.is_valid_password(passwordCredential):
            from api.v1.app import auth
            sessionId = auth.create_session(user.id)
            respond = jsonify(user.to_json())
            respond.set_cookie(sessionName, sessionId)
            return respond
    return jsonify({"error": "wrong password"}), 401


@app_views.route('/auth_session/logout',
                 methods=['DELETE'],
                 strict_slashes=False)
def delete_session():
    """
    destroy session cookie
    """
    from api.v1.app import auth
    if not auth.destroy_session(request):
        return False, 404
    return jsonify({}), 200
