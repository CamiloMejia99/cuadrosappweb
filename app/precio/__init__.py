from flask import Blueprint

precio = Blueprint('precio', __name__, template_folder='templates')

from . import routes

