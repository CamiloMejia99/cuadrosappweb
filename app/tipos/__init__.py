from flask import Blueprint

tipo = Blueprint('tipo', __name__, template_folder='templates')

from . import routes

