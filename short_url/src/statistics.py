
from flask import Blueprint, jsonify, redirect, request
from sqlalchemy import true
from src.database import db, UrlVisitors, UrlShortener
from src.auth import get_check_token
from http import HTTPStatus
from flasgger import Swagger, swag_from
from src.config.swagger import template, swagger_config
from flask_paginate import Pagination, get_page_parameter, get_per_page_parameter


stats = Blueprint("stats", __name__, url_prefix="/api/v1/statistics")


@stats.get('/')
@swag_from('./docs/stats.yaml')
def get_stats():
    token = request.headers.get("Authorization").split()[-1]
    if get_check_token(token):
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 2, type=int)

        created_url = UrlShortener.query.filter_by().paginate(page=page, per_page=per_page)

        data = []

        all_items = UrlShortener.query.filter_by().order_by(UrlShortener.visits_count.desc()).paginate(page=page, per_page=per_page)

        for item in all_items.items:
            view_stats = {
                'id': item.id,
                'Site URL': item.url,
                'Visits count': item.visits_count,
                'Date Created': item.created_at

            }
            
            data.append(view_stats)

        meta = {
            "page": created_url.page,
            'pages': created_url.pages,
            'total_count': created_url.total,
            'prev_page': created_url.prev_num,
            'next_page': created_url.next_num,
            'has_next': created_url.has_next,
            'has_prev': created_url.has_prev,
        }
    
        
        return jsonify({'data':data, 'meta': meta}), HTTPStatus.OK
    return jsonify({"message": "Unauthorized"}), HTTPStatus.UNAUTHORIZED
    



@stats.get('<int:id>')
@swag_from('./docs/stats_for_id.yaml')
def get_stats_id(id):
    token = request.headers.get("Authorization").split()[-1]
    if get_check_token(token):
        data = []

        items = UrlVisitors.query.filter_by(id=id).order_by(UrlVisitors.device_visits_count.desc()).all()

        for item in items:
            view_stats = {
                'id': item.id,
                'User ID': item.user_id,
                'Device IP': item.device_ip,
                'Device visits count': item.device_visits_count,
                'Date Created': item.device_visit_date

            }
            data.append(view_stats)

        return jsonify({'data':data}), HTTPStatus.OK
    return jsonify({"message": "Unauthorized"}), HTTPStatus.UNAUTHORIZED