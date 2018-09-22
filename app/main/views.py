from . import main

from flask import render_template

from ..decorators import admin_required,permission_required
from ..models import Permission,User
from flask_login import login_required



@main.route('/')
def index():
    return render_template('main/index.html')

@main.route('/admin')
@login_required
@admin_required
def admin():
    return 'admin only'

@main.route('/user/<username>')
def user(username):
    user=User.query.filter_by(username=username).first_or_404()
    return render_template('user.html',user=user)