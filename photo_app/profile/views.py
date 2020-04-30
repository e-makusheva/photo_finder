from flask import abort, Blueprint, flash, current_app, render_template, redirect, url_for
from flask_login import current_user, login_required

from photo_app.profile.forms import ProfileForm
from photo_app.profile.models import Profile
from photo_app import db

blueprint = Blueprint('profile', __name__, url_prefix='/profiles')

@blueprint.route('/<int:profile_id>')
def profile(profile_id):
    my_profile = Profile.query.filter(Profile.profile_id == profile_id).first()
    if not my_profile:
        abort(404)
    return render_template('profile/my_profile.html', profile=profile)

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
        #return redirect(url_for 'profile.')
    flash('Пожалуйста, исправьте ошибки')
    return redirect(url_for('profile.edit_profile'))

