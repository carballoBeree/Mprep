from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from musica.db import get_db

bp = Blueprint('album', __name__, url_prefix='/albums')

@bp.route('/')
def index():
    db = get_db()
    lista_albums = db.execute(
        """SELECT Title as albums FROM albums"""
    ).fetchall()
    return render_template('albums.html', album=lista_albums)