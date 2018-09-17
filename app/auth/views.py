from . import auth
from .forms import *
from flask import render_template,redirect,url_for,request,flash
from ..models import User
from flask_login import login_user,login_required,logout_user,current_user
from app import db
from ..email import send_email,send_async_email


@auth.route('/login',methods=['GET','POST'])
def login():
    login_form=LoginFrom()
    if login_form.validate_on_submit():
        user=User.query.filter_by(email=login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))#类似中断返回
        flash('错误的用户名或密码')
    return render_template('auth/login.html',form=login_form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('白白！')
    return redirect(url_for('main.index'))

@auth.route('/register',methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        user=User(email=form.email.data,
                  username=form.username.data,
                  password=form.password.data)
        db.session.add(user)
        db.session.commit()
        token=user.generate_confirmation_token()
        send_email(user.email,'确认账号','auth/email/confirm',user=user,token=token)
        flash('确认邮件已发送至你的邮箱，请及时确认（1h）')
        return redirect(url_for('main.index'))
    return render_template('auth/register.html',form=form)


@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        flash('确认成功')
    else:
        flash('链接失效')
    return redirect(url_for('main.index'))

@auth.before_app_request
def before_request():
    if current_user.is_authenticated \
            and not current_user.confiremed \
            and request.endpoint[:5] !='auth.' \
            and request.endpoint != 'static':
        return redirect(url_for('auth.unconfirmed'))

@auth.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:
        return redirect(url_for('main.index'))
    return render_template('auth/unconfirmed.html')

@auth.route('/confirm')
@login_required
def resend_conformation():
    token = current_user.generate_confirmation_token()
    send_email(current_user.email, '确认账号', 'auth/email/confirm',
               user=current_user, token=token)
    flash('新确认邮件已发送至你的邮箱，请及时确认（1h）')
    return redirect(url_for('main.index'))
