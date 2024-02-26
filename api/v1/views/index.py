#!/usr/bin/python3
"""
import app_views from api.v1.views
"""
from flask import jsonify
from api.v1.views import app_views


@app_views.route("/status")
def get_status():
    """ returns the status of API:
    """
    return jsonify(status='OK')
