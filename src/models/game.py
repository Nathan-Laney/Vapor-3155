from models import db
from datetime import datetime
# from sqlalchemy.dialects.postgresql import JSON

class game(db.Model):  # type: ignore
    __tablename__ = 'game'
    
    game_id =           db.Column(db.Integer, primary_key=True)
    title =             db.Column(db.String, nullable=False)
    publisher =         db.Column(db.String, nullable=True)
    description =       db.Column(db.String, nullable=True)
    developer =         db.Column(db.String, nullable=True)
    thumbnail_link =    db.Column(db.String, nullable=True)
    release_date =      db.Column(db.DateTime, nullable=False)
