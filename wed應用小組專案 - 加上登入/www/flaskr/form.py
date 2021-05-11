from flaskr.model import UserRegister
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, PasswordField, ValidationError, BooleanField
from wtforms.fields.html5 import EmailField


class FormRegister(FlaskForm):
    """ 依照Model來建置相對應的Form  """
    name = StringField('姓名', validators=[
        validators.DataRequired(),
        validators.Length(1, 50)
    ])
    username = StringField('帳號', validators=[
        validators.DataRequired(),  # 限制為必填
        validators.Length(4, 30)  # 限制最短要8個字，最長30個字
    ])
    email = EmailField('Email', validators=[
        validators.DataRequired(),
        validators.Length(1, 50),
        validators.Email()
    ])
    password = PasswordField('密碼', validators=[
        validators.DataRequired(),
        validators.Length(5, 10),
        validators.EqualTo('password2', message='密碼需要符合上欄輸入')
    ])
    password2 = PasswordField('密碼（請重複一次）', validators=[
        validators.DataRequired()
    ])
    submit = SubmitField('建立帳號')


    def validate_email(self, field):
        if UserRegister.query.filter_by(email=field.data).first():
            raise ValidationError('信箱已被註冊')

    def validate_username(self, field):
        if UserRegister.query.filter_by(username=field.data).first():
            raise ValidationError('使用者名稱已被註冊')


class FormLogin(FlaskForm):
    """
    使用者登入使用，以email為主要登入帳號，密碼需做解碼驗證
    """
    email = EmailField('Email', validators=[
        validators.DataRequired(),
        validators.Length(5, 30),
        validators.Email()
    ])
    password = PasswordField('密碼', validators=[
        validators.DataRequired()
    ])
    remember_me = BooleanField('記住我')
    submit = SubmitField('登入')


