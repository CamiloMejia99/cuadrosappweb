from flask import Blueprint

carritocompras = Blueprint('carritocompras', __name__, template_folder='templates')

from . import routes 

