import re

from flask import session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError

from App.models import User


def check_phone(form1, field):
    if not re.match(r'(13\d|14[5|7]|15\d|166|17[3|7]|18\d)\d{8}$', field.data):
        raise ValidationError("电话号码不符合规则")


# 图片验证码
def validate_piccode(form2, field):
    if field.data != session['code']:
        raise ValidationError('验证码匹配失败')

# 手机短信验证
def validate_phonecode(form3, field):
    print(field.data, session.get("sms"))
    if field.data != session.get("sms"):
        raise ValidationError("短信验证失败")


# 验证用户是否重名
def validate_nickname(form4, field):
    # value是一个对象，获取用户输入的值应该是field.data
    user = User.query.filter(User.username == field.data).first()
    if user:
        raise ValidationError("用户名重名")
    return field

class RegisterForm(FlaskForm):
    nickname = StringField(validators=[DataRequired("用户名必须输入"), Length(min=6, max=12, message="用户名长度必须在6-12位"),validate_nickname])
    password = PasswordField(validators=[DataRequired("密码必须输入"), Length(min=8, max=20, message="密码长度必须在8-20位")])
    pwdagain = PasswordField(validators=[EqualTo("password", message="两次密码不一致"),DataRequired("密码必须输入")])
    phonenum = StringField(validators=[check_phone])
    piccode = StringField(validators=[DataRequired('验证码必须输入'),validate_piccode])
    phonecode = StringField(validators=[DataRequired('验证码必须输入'),validate_phonecode])
    submit = SubmitField(label="注册")
    #
    # # 验证用户是否重名
    # # 自定义的验证方法： validate_字段名
    # def validate_nickname(self, field):
    #     # value是一个对象，获取用户输入的值应该是field.data
    #     user = User.query.filter(User.username == field.data).first()
    #     if user:
    #         raise ValidationError("用户名重名")
    #     return field

    # # 图片验证码
    # def validate_piccode(self, field):
    #     if field.data != session['code']:
    #         raise ValidationError('验证码匹配失败')
    #
    # # 手机短信验证
    # def validate_sms(self, field):
    #     print(field.data, session.get("sms"))
    #     if field.data != session.get("sms"):
    #         raise ValidationError("短信验证失败")
