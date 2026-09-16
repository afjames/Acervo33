from app import db

class Album(db.model):
    __tablename__ = 'albuns'

    id = db.Column(db.Integer, primary_key=True, autoincremente=True)