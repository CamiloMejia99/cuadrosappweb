from flask import Blueprint

queja = Blueprint('queja', __name__, template_folder='templates')

from . import routes 

