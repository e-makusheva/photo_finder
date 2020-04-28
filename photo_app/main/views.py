from flask import Blueprint, current_app, render_template, request
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired

from photo_app import db
from photo_app.user.models import User

blueprint = Blueprint('main_page', __name__)

@blueprint.route('/')
def index():
    title = 'Photo Finder'
    return render_template('index.html', page_title=title)

def profiles():
    profile_list = User.query.filter(User.roles == 'photographer')

