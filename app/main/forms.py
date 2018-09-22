from flask_wtf import Form
from wtforms import StringField,SubmitField,TextAreaField,BooleanField,SelectField
from wtforms.validators import Length, DataRequired, Email, Regexp,ValidationError

from app.models import Role, User


class EditProfileForm(Form):
    name=StringField('真实姓名',validators=[Length(0,64)])
    location=StringField('所在地',validators=[Length(0,64)])
    about_me=TextAreaField('自述')
    submit=SubmitField('保存')

class EditProfileAdminForm(Form):
    email=StringField('邮箱',validators=[DataRequired(),Length(1,64),Email()])
    username=StringField('昵称',validators=[DataRequired(),Length(1,64),
                                          Regexp('^[A-Za-z0-9_.]*$',0,
                                                 '不好意思，为了存储方便，只接受字母，下划线和点')])

    confirmed=BooleanField('激活')
    role=SelectField('角色',coerce=int)
    name=StringField('真实姓名',validators=[Length(0,64)])
    location=StringField('地址',validators=[Length(0,64)])
    about_me = TextAreaField('自述')
    submit = SubmitField('确定')

    def __init__(self,user,*args,**kwargs):
        super(EditProfileAdminForm,self).__init__(*args,**kwargs)
        self.role.choices=[(role.id,role.rolename)
                           for role in Role.query.order_by(Role.rolename).all()]
        self.user=user

    def validate_email(self,field):
        if field.data != self.user.email and \
            User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已经激活过')

    def valisate_username(self,field):
        if field.data != self.user.username and \
            User.query.filter_by(username=field.data).first():
            raise ValidationError('昵称已被用')