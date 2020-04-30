from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

class ProfileForm(FlaskForm):
    user_id = HiddenField('ID пользователя', validators=[DataRequired()])
    city = StringField('Город', validators=[DataRequired()], render_kw={"class": "input100"})
    about = StringField('О себе', validators=[DataRequired()], render_kw={"class": "input100"})
    Instagram = StringField('Адрес страницы в Instagram', validators=[DataRequired()], render_kw={"class": "input100"})
    contacts = StringField('Контакты', validators=[DataRequired()], render_kw={"class": "input100"})
    submit = SubmitField('Сохранить', render_kw={"class": "btn btn-primary"})
