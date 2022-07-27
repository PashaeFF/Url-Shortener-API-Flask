from flask import Blueprint, jsonify, redirect, request
from src.database import db, UrlVisitors, UrlShortener
from user_agents import parse
import requests
from flasgger import swag_from
from src.config.swagger import template, swagger_config
import socket


short_url_api = Blueprint("short_url_api", __name__)


@short_url_api.get('/<short_url>')
@swag_from('./docs/visits.yaml')
def redirect_to_url(short_url):
    if "favicon.ico" == short_url:
        return jsonify({})
    link = UrlShortener.query.filter_by(short_url=short_url).first()
    if link:
        r = requests.get('http://google.com')
        agent = r.request.headers.get('User-Agent') #user agent
        where = "" #It shows which link the user came from
        ip_address = '12.12.1.26' #user IP
        user = "af83b713-d2a1-4f1e-bc37-2ddd270d2db5" #user UUID
        r.status_code

        updated = UrlVisitors.query.filter_by(url_id=link.id, where = "link", browser_info = agent, device_ip = ip_address, user_id = user).first()

        if not updated:
            visitor = UrlVisitors(url_id=link.id, where = "link", browser_info = agent, device_ip=ip_address, user_id = user)
            link.visits_count += 1
            print("visitor")
        
            db.session.add(visitor)
            db.session.commit()

        else:
            updated.device_visits_count += 1
            print("2")
            db.session.add(updated)
            
            db.session.commit()
        return redirect(link.url)
    else:
        return jsonify({'error':'Not Found'})
        
        


