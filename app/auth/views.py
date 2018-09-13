from . import auth
from .forms import *
from flask import render_template,redirect,url_for

@auth.route('/login')
def login():
    form=LoginFrom()
    if form.validate_on_submit():
        return redirect(url_for('.login'))
    return render_template('base.html')