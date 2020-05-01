from flask import abort, Blueprint, flash, current_app, render_template, redirect, request, url_for
from flask_login import current_user, login_required

from photo_app.profile.forms import ProfileForm
from photo_app.profile.models import Profile
from photo_app import db

blueprint = Blueprint('profile', __name__, url_prefix='/profile')

@blueprint.route('/profile')
def profile(user_id):
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
        new_profile = Profile(user_id=current_user.id, city=profile_form.city.data, about=profile_form.about.data, Instagram=profile_form.Instagram.data, contacts=profile_form.contacts.data)
        db.session.add(new_profile)
        db.session.commit()
        flash('Профиль успешно заполнен')
        return redirect(request.referer)
    flash('Пожалуйста, исправьте ошибки')
    return redirect(url_for('profile.edit_profile'))

