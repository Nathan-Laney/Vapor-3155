from models import db
from datetime import datetime
# from sqlalchemy.dialects.postgresql import JSON

class review(db.Model):  # type: ignore
    __tablename__ = 'review'
    
    review_id =             db.Column(db.Integer, primary_key=True)
    author_id =             db.Column(db.Integer, primary_key=False)
    game_id =               db.Column(db.Integer, primary_key=False)
    date =                  db.Column(db.DateTime, nullable=False)
    rating_score =          db.Column(db.Integer, nullable=False)
    replayability_score =   db.Column(db.Integer, nullable=True)
    graphics_score =        db.Column(db.Integer, nullable=True)
    description =           db.Column(db.String, nullable=False)
