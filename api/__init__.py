import shelve

from flask import Flask, g
from .games import getAllGames

app = Flask(__name__)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("games.db")
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route("/games")
def games_index():
    db = get_db()
    return getAllGames(db)
