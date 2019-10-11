from flask import Blueprint

bp = Blueprint('ping',__name__,url_prefix='/api')

from app.api import ping,users
