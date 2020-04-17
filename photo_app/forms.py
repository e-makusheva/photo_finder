from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()], render_kw={"class": "wrap-input100 validate-input m-b-16"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "wrap-input100 validate-input m-b-16"})
    submit = SubmitField('Войти', render_kw={"class": "login100-form-btn"})
