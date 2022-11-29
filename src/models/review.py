from models import db
from datetime import datetime
# from sqlalchemy.dialects.postgresql import JSON

class review(db.Model):  # type: ignore
    __tablename__ = 'review'
    
    review_id =             db.Column(db.Integer, primary_key=True)
    date =                  db.Column(db.DateTime, nullable=False)
    rating_score =          db.Column(db.Integer, nullable=False)
    replayability_score =   db.Column(db.Integer, nullable=True)
    graphics_score =        db.Column(db.Integer, nullable=True)
    description =           db.Column(db.String, nullable=False)

    def __init__(self, title: str,  publisher: str, description: datetime, developer: str, thumbnail_link: str) -> None:
        self.title = title
        self.publisher = publisher
        self.description = description
        self.developer = developer
        self.thumbnail_link = thumbnail_link
