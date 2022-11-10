from flask import Blueprint 
from .view import index
from .view import login 

bp = Blueprint('web',__name__,template_folder='templates')

bp.add_url_rule('/',view_func=index)
bp.add_url_rule('/login',view_func=login)

def init_app(app):
    app.register_blueprint(bp)