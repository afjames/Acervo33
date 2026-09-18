from app import db

class MidiaFisica(db.Model):
    __tablename__ = 'midia_fisica'

    id = db.Column(db.Integer, primary_key=True)
    formato = db.Column(db.String(20), nullable=False)
    estado_conservacao = db.Column(db.String(50))
    album_id = db.Column(db.Integer, db.ForeignKey('albuns.id'), nullable=False)

    
    def to_dict(self):
        return {
            'id': self.id,
            'formato': self.formato,
            'estado_conservacao': self.estado_conservacao,
            'album_id': self.album_id
        }
