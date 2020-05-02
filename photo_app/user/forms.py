from flask_wtf import FlaskForm
from wtforms import BooleanField, HiddenField, StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from photo_app.user.models import User

class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()], render_kw={"class": "input100"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "input100"})
    remember_me = BooleanField('Запомнить', default=True, render_kw={"class": "input-checkbox100"})
    submit = SubmitField('Войти', render_kw={"class": "login100-form-btn"})

class RegistrationForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()], render_kw={"class": "input--style-3"})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"class": "input--style-3"})
    password = PasswordField('Введите пароль', validators=[DataRequired()], render_kw={"class": "input--style-3"})
    password_check = PasswordField(
        'Повторите пароль', validators=[DataRequired(), EqualTo('password')], render_kw={"class": "input--style-3"})
    roles = SelectField('Выберите деятельность', choices=[('no_change', 'Не выбрано'), ('photographer', 'Фотограф'), ('user', 'Заказчик')], render_kw={"class": "rs-select2 js-select-simple select--no-search"})
    submit = SubmitField('Подтвердить', render_kw={"class": "btn btn--pill btn--green"})

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Такой логин уже существует')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Такой email уже существует')

class ProfileForm(FlaskForm):
    profile_id = HiddenField('ID пользователя', validators=[DataRequired()])
    fullname = StringField('Полное имя', validators=[DataRequired()], render_kw={"class": "input100"})
    city = StringField('Город', validators=[DataRequired()], render_kw={"class": "input100"})
    about = StringField('О себе', validators=[DataRequired()], render_kw={"class": "input100"})
    Instagram = StringField('Адрес страницы в Instagram', validators=[DataRequired()], render_kw={"class": "input100"})
    contacts = StringField('Контакты', validators=[DataRequired()], render_kw={"class": "input100"})
    submit = SubmitField('Сохранить', render_kw={"class": "btn btn-primary"})
