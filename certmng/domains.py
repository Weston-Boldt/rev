from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify, make_response
)
from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('domain', __name__)

@bp.route('/domains/<string:domain>', methods=['GET', 'POST'])
def domains():
    if method == 'POST':
        error = validate_domain(domain)
        if (error):
            return make_response()
        add_domain(domain)
    else:
        pass


def validate_domain(domain=None):
    if not domain:
        return "no domain"
