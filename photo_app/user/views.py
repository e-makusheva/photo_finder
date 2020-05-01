from flask import abort, Blueprint, flash, render_template, request, redirect, url_for
from flask_login import current_user, login_user, logout_user

from photo_app.user.forms import LoginForm, ProfileForm, RegistrationForm
from photo_app.user.models import User, Profile
from photo_app import db

blueprint = Blueprint('user', __name__, url_prefix='/users')

@blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main_page.index'))
    title = 'Авторизация'
    login_form = LoginForm()
    return render_template('user/login.html', page_title=title, form=login_form)

@blueprint.route('/process-login', methods=['POST'])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('Вы вошли на сайт')
            return redirect(url_for('main_page.index'))
    flash('Неправильный логин или пароль')
    return redirect(url_for('user.login'))

@blueprint.route('/logout')
def logout():
    logout_user()
    flash('Вы успешно разлогинились')
    return redirect(url_for('main_page.index'))

@blueprint.route('/register')
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main_page.index'))
    title = 'Регистрация'
    form = RegistrationForm()
    return render_template('user/registration_form.html', page_title=title, form=form)

@blueprint.route('/process-reg', methods=['POST'])
def process_reg():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, roles=form.roles.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Регистрация прошла успешно')
        return redirect(url_for('user.login'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Ошибка в поле "{}": - {}'.format(
                    getattr(form, field).label.text,
                    error
                ))
        return redirect(url_for('user.register'))
    flash('Пожалуйста, исправьте ошибки')
    return redirect(url_for('user.register'))

@blueprint.route('/profile')
def profile():
    my_profile = Profile.query.filter(Profile.user_id == current_user.id).first()
    if not my_profile:
        abort(404)
    return render_template('profile/profile.html', about=my_profile.about, profile=my_profile)

@blueprint.route('/edit_profile')
def edit_profile():
    profile_form = ProfileForm()
    return render_template('profile/edit_profile.html', form=profile_form)
        
@blueprint.route('/process_edit', methods=['POST'])
def process_edit():
    profile_form = ProfileForm()
    if profile_form.validate_on_submit():
        new_profile = Profile(city=profile_form.city.data, about=profile_form.about.data, Instagram=profile_form.Instagram.data, contacts=profile_form.contacts.data)
        db.session.add(new_profile)
        db.session.commit()
        flash('Профиль успешно заполнен')
        return redirect(url_for('main_page.index')
    flash('Пожалуйста, исправьте ошибки')
    return redirect(url_for('profile.edit_profile'))

