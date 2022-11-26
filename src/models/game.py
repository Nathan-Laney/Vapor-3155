from models import db
# from sqlalchemy.dialects.postgresql import JSON

class Game(db.Model):
    __tablename__ = 'game'
    
    game_id =           db.Column(db.Integer, primary_key=True)
    title =             db.Column(db.String, nullable=False)
    publisher =         db.Column(db.String, nullable=True)
    description =       db.Column(db.String, nullable=True)
    developer =         db.Column(db.String, nullable=True)
    thumbnail_link =    db.Column(db.String, nullable=True)

    def __init__(self, title: str,  publisher: str, description: str, developer: str, thumbnail_link: str) -> None:
        self.title = title
        self.publisher = publisher
        self.description = description
        self.developer = developer
        self.thumbnail_link = thumbnail_link
