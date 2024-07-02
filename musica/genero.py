from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from musica.db import get_db

bp = Blueprint('genero', __name__, url_prefix='/generos')

@bp.route('/')
def index():
    db = get_db()
    lista_generos = db.execute(
        """SELECT Name as generos FROM genres"""
    ).fetchall()
    return render_template('generos.html', genre=lista_generos)