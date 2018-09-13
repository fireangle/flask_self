from flask import Flask
from config import config

from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *

from flask_sqlalchemy import SQLAlchemy


bootstrap=Bootstrap()
nav = Nav()

db=SQLAlchemy()

@nav.navigation()
def create_navbar():
    home_view=View(u'主页', 'auth.login')
    tool_view=View(u'工具', 'auth.login')
    catelog_view=View(u'分类', 'auth.login')
    login_view=Link('登录','login')
    project_view=View('项目', 'auth.login')
    about_view=View('关于', 'auth.login')
    work_subgroup=Subgroup('工作区',
                           project_view,
                           tool_view)
    return Navbar('fireangle',
                  home_view,catelog_view,work_subgroup,
                  about_view,login_view)


def create_app(config_name):
    app=Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    nav.register_element('mybar',create_navbar())
    nav.init_app(app)
    bootstrap.init_app(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/auth')

    db.init_app(app)

    return app
