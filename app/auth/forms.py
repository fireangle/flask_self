from flask_wtf import Form
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Length,Email,Regexp,EqualTo
from ..models import User
from wtforms import ValidationError


class LoginFrom(Form):
    email=StringField('邮箱',validators=[DataRequired(),Length(1,64),Email()])
    password=PasswordField('密码',validators=[DataRequired()])
    remember_me=BooleanField('不要忘了我哦')
    submit=SubmitField('提交')

class RegistrationForm(Form):
    email=StringField('邮箱',validators=[DataRequired(),Length(1,64),Email()])
    username=StringField('昵称',validators=[DataRequired(),Length(1,64),
                                          Regexp('^[A-Za-z0-9_.]*$',0,
                                                 '不好意思，为了存储方便，只接受字母，下划线和点')])

    password=PasswordField('密码',validators=[DataRequired()])
    password2 = PasswordField('确认密码',validators=[DataRequired(),EqualTo('password',
                                                                        message='不一致')])
    submit=SubmitField('注册')

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已注册')

    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('昵称已被用')
