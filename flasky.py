from flask import Flask, render_template, redirect, url_for
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar,View


app=Flask(__name__)
bootstrap=Bootstrap(app)
nav=Nav()
nav.register_element('top',Navbar(u'fireangle',
                                  View(u'主页','index'),
                                  View(u'工具', 'index'),
                                  View(u'作者', 'index')))
nav.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('test.html')

manage=Manager(app)

if __name__=='__main__':
    manage.run()