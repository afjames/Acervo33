from app import db

class Artista(db.Model):
    __tablename__ = 'artistas'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return{
            'id': self.id,
            'nome': self.nome
        }