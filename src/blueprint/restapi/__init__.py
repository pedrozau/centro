from flask import Blueprint 
from flask_restx import Api 
from .resource import UserRoute



bp =  Blueprint('restapi',__name__,url_prefix='/api/v1')

api = Api(bp)

api.add_resource(UserRoute,'/users')


def init_app(app):
    app.register_blueprint(bp)



