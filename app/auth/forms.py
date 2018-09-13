from flask_wtf import  Form
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired


class LoginFrom(Form):
    username=StringField('姓名',validators=[DataRequired()])
    submit=SubmitField('提交')