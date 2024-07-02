from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from musica.db import get_db

bp = Blueprint('track', __name__, url_prefix='/tracks')

@bp.route('/')
def index():
    db = get_db()
    lista_tracks = db.execute(
        """SELECT Name FROM tracks"""
    ).fetchall()
    return render_template('tracks.html', track=lista_tracks)