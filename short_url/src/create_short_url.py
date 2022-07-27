from flask import Blueprint, current_app, request
from http import HTTPStatus
from flask.json import jsonify
from src.database import UrlShortener, db
from src.auth import get_check_token
from flasgger import Swagger, swag_from
from src.config.swagger import template, swagger_config
import validators


created_url = Blueprint("url",__name__,
url_prefix="/api/v1/url")

@created_url.route('', methods = ['POST'])
@swag_from('./docs/shortener.yaml')
def handle_short_url():
    token = request.headers.get("Authorization").split()[-1]
    if get_check_token(token):
        if request.method == 'POST':
            url_title = request.get_json().get('url_title','')
            url = request.get_json().get('url','')

            if not validators.url(url):
                return jsonify({
                    'error': 'Duzgun url qeyd edin...'
                }), HTTPStatus.BAD_REQUEST

            if UrlShortener.query.filter_by(url=url).first():
                return jsonify({
                    'error': 'URL movcuddur'
                }), HTTPStatus.CONFLICT
            
            created_url = UrlShortener(url=url, url_title=url_title)
            db.session.add(created_url)
            db.session.commit()

            return jsonify({

                'id': created_url.id,
                'url_title': created_url.url_title,
                'url': created_url.url,
                'short_url': created_url.short_url,
                'created_at': created_url.created_at,
                'updated_at': created_url.updated_at
                
            }), HTTPStatus.CREATED
    return jsonify({"message": "Unauthorized"}), HTTPStatus.UNAUTHORIZED

@created_url.get("/<int:id>")
@swag_from('./docs/get_short_url.yaml')
def get_created_url(id):
    print(current_app.config["SQLALCHEMY_MAX_OVERFLOW"])
    token = request.headers.get("Authorization").split()[-1]
    if get_check_token(token):
        created_url = UrlShortener.query.filter_by(id=id).first()

        if not created_url:
            return jsonify({'message': 'Item not found'}), HTTPStatus.NOT_FOUND

        return jsonify({
                'id': created_url.id,
                'url_title': created_url.url_title,
                'url': created_url.url,
                'short_url': created_url.short_url,
                'created_at': created_url.created_at,
                'updated_at': created_url.updated_at
                
        }), HTTPStatus.OK
    return jsonify({"message": "Unauthorized"}), HTTPStatus.UNAUTHORIZED


@created_url.delete("/<int:id>")
def delete_created_url(id):
    token = request.headers.get("Authorization").split()[-1]
    if get_check_token(token):
        created_url = UrlShortener.query.filter_by(id=id).first()

        if not created_url:
            return jsonify({'message': 'item not found'}), HTTPStatus.NOT_FOUND

        db.session.delete(created_url)
        db.session.commit()

        return jsonify({'message': 'Silindi'}), HTTPStatus.NO_CONTENT
    return jsonify({"message": "Unauthorized"}), HTTPStatus.UNAUTHORIZED

@created_url.put('/<int:id>')
@created_url.patch('/<int:id>')
def edit_created_url(id):
    token = request.headers.get("Authorization").split()[-1]
    if get_check_token(token):
        created_url = UrlShortener.query.filter_by(id=id).first()

        if not created_url:
            return jsonify({'message': 'item not found'}), HTTPStatus.NOT_FOUND

        url_title = request.get_json().get('url_title','')
        url = request.get_json().get('url','')

        if not validators.url(url):
            return jsonify({
                'error': 'Duzgun url qeyd et'
            }), HTTPStatus.BAD_REQUEST

        if UrlShortener.query.filter_by(url=url).first():
            return jsonify({
                'error': 'URL movcuddur'
            }), HTTPStatus.CONFLICT

        created_url.url = url
        created_url.url_title = url_title

        db.session.commit()

        return jsonify({

                'id': created_url.id,
                'url_title': created_url.url_title,
                'url': created_url.url,
                'short_url': created_url.short_url,
                'created_at': created_url.created_at,
                'updated_at': created_url.updated_at
                
            }), HTTPStatus.OK
    return jsonify({"message": "Unauthorized"}), HTTPStatus.UNAUTHORIZED