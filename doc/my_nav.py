from flask_nav.elements import *
from app import nav


class Login_bar(Text):
    def __init__(self):
        pass

    @property
    def text(self):
        return '1'


@nav.navigation()
def create_nav_login():
    a=Login_bar()
    home_view=View(u'主页', 'auth.login')
    tool_view=View(u'工具', 'auth.login')
    catelog_view=View(u'分类', 'auth.login')
    login = View('登录', 'auth.login')
    project_view=View('项目', 'auth.login')
    about_view=View('关于', 'auth.login')
    work_subgroup=Subgroup('工作区',
                           project_view,
                           tool_view)

    return Navbar('fireangle',
                  home_view,catelog_view,work_subgroup,
                  about_view,login,a)

@nav.navigation()
def create_nav_logout():
    home_view=View(u'主页', 'auth.login')
    tool_view=View(u'工具', 'auth.login')
    catelog_view=View(u'分类', 'auth.login')
    logout = View('退出', 'auth.login')
    project_view=View('项目', 'auth.login')
    about_view=View('关于', 'auth.login')
    work_subgroup=Subgroup('工作区',
                           project_view,
                           tool_view)

    return Navbar('fireangle',
                  home_view,catelog_view,work_subgroup,
                  about_view,logout)
