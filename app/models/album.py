from app import db

class Album(db.Model):
    __tablename__ = 'albuns'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(100), nullable=False)
    ano_lancamento = db.Column(db.SmallInteger, nullable=False)
    genero = db.Column(db.String(50), nullable=False)
    duracao_album = db.Column(db.Time, nullable=False)
    nota = db.Column(db.SmallInteger)
    capa_url = db.Column(db.String(255))

    artista_id = db.Column(db.Integer, db.ForeignKey('artistas.id'), nullable=False)

    def to_dict(self):
        return {
          'id': self.id,
            'titulo': self.titulo,
            'ano_lancamento': self.ano_lancamento,
            'genero': self.genero,
            'duracao_album': str(self.duracao_album) if self.duracao_album else None,
            'nota': self.nota,
            'capa_url': self.capa_url,
            'artista_id': self.artista_id  
        }
