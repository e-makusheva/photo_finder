from flask import Blueprint

from photo_app.user.decorators import admin_required

blueprint = Blueprint('admin', __name__, url_prefix='/admin')

@blueprint.route('/')
@admin_required
def admin_index():
    return 'Доступ разрешён'
