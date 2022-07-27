from flask import Flask, jsonify
import os
from http import HTTPStatus
from src.url_visits import short_url_api
from src.database import db
from src.create_short_url import created_url
from src.statistics import stats
from flask_migrate import Migrate
from flasgger import Swagger
from src.config.swagger import template, swagger_config
from src.settings.app_settings import app_settings


def create_app():

    app = Flask(__name__, instance_relative_config=True)

    # app.config.from_mapping(
    #     SECRET_KEY=os.environ.get
    #     ("SECRET_KEY"),
    #     SQLALCHEMY_DATABASE_URI=os.environ.get
    #     ("SQLALCHEMY_DB_URI"),
    #     SQLALCHEMY_TRACK_MODIFICATIONS = False,
    #     SWAGGER = {
    #         'title':"URL Shortener API",
    #     },
    #     SQLALCHEMY_MAX_OVERFLOW=True
    # )

    app.config.from_object(app_settings)
    

    db.app = app
    db.init_app(app)
    Migrate(app,db)

    app.register_blueprint(short_url_api)
    app.register_blueprint(created_url)
    app.register_blueprint(stats)
    Swagger(app, config=swagger_config,template=template,)

    @app.errorhandler(HTTPStatus.NOT_FOUND)
    def handle_404(error):
        return jsonify({'error': error.description}), HTTPStatus.NOT_FOUND

    @app.errorhandler(HTTPStatus.INTERNAL_SERVER_ERROR)
    def handle_500(error):
        return jsonify({'error': error.description}), HTTPStatus.INTERNAL_SERVER_ERROR

    
    return app