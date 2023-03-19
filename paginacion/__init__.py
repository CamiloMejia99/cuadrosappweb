from flask import Blueprint

paginacion = Blueprint('paginacion', __name__, template_folder='templates')

from . import routes

