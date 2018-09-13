from flask import Flask

from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *



bootstrap=Bootstrap()

nav = Nav()

def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']='556'
    nav.register_element('top', Navbar(u'fireangle',
                                       View(u'主页', 'auth.login'),
                                       View(u'工具', 'auth.login'),
                                       View(u'作者', 'auth.login'),
                                       View(u'分类', 'auth.login'),
                                       Subgroup('更多',
                                                View('1', 'auth.login'),
                                                View(u'分类', 'auth.login'), )))
    nav.init_app(app)
    bootstrap.init_app(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/auth')

    return app
