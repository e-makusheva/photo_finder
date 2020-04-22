from flask import Blueprint, current_app, render_template

blueprint = Blueprint('main_page', __name__)

@blueprint.route('/')
def index():
    title = 'Photo Finder'
    return render_template('index.html', page_title=title)