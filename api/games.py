import os


def getAllGames(db):
    return {"message": "success", "data": os.environ.get('API_ENV')}, 200
