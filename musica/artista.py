from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from musica.db import get_db

bp = Blueprint('artista', __name__, url_prefix='/artistas')

@bp.route('/')
def index():
    db = get_db()
    lista_artistas = db.execute(
        """SELECT Name as artistas FROM artists"""
    ).fetchall()
    return render_template('artistas.html', artist=lista_artistas)
