from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from photo_app.user.models import User

class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()], render_kw={"class": "wrap-input100 validate-input m-b-16"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "wrap-input100 validate-input m-b-16"})
    remember_me = BooleanField('Запомнить', default=True, render_kw={"class": "input-checkbox100"})
    submit = SubmitField('Войти', render_kw={"class": "login100-form-btn"})

class RegistrationForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()], render_kw={"class": "input--style-3"})
    email = StringField('E-mail', validators=[DataRequired(), Email()], render_kw={"class": "input-group"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "input-group"})
    password_check = PasswordField(
        'Повторите пароль', validators=[DataRequired(), EqualTo('password')], render_kw={"class": "input-group"})
    role = SelectField('Выберите деятельность', choices=[('no_change', 'Не выбрано'), ('photographer', 'Фотограф'), ('user', 'Заказчик')], render_kw={"class": "rs-select2 js-select-simple select--no-search"})
    submit = SubmitField('Регистрация', render_kw={"class": "p-t-10"})

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Такой логин уже существует')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Такой email уже существует')