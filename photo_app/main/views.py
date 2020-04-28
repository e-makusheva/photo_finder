from flask import Blueprint, current_app, render_template, request

from photo_app import db
from photo_app.user.models import User

blueprint = Blueprint('main_page', __name__)

@blueprint.route('/')
def index():
    title = 'Photo Finder'
    profile_list = User.query.filter(User.roles == 'photographer')
    return render_template('index.html', page_title=title)

