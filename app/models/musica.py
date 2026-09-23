from app import db

class Musica(db.Model):
    __tablename__ = 'musicas'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    faixa_numero = db.Column(db.Integer, nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey('albuns.id'), nullable=False)
    favorita = db.Column(db.Boolean, default=False)


    def to_dict(self):
        return {
            'id':self.id,
            'titulo':self.titulo,
            'faixa_numero':self.faixa_numero,
            'favorita':self.favorita,
            'album_id':self.album_id
        }