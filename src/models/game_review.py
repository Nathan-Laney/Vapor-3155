from models import db

# from sqlalchemy.dialects.postgresql import JSON

class game_review(db.Model):  # type: ignore
    __tablename__ = 'game_review'
    
    review_id =        db.Column(db.Integer, db.ForeignKey("review.review_id", ondelete="CASCADE", onupdate="CASCADE"), primary_key = True)
    review_rel = db.relationship("review", backref = "review")


    game_id =        db.Column(db.Integer, db.ForeignKey("game.game_id", ondelete="CASCADE", onupdate="CASCADE"), primary_key = True)
    game_rel = db.relationship("game", backref = "game")

    def __init__(self, tag_id:int, review_id:int) -> None:
        self.tag_id = tag_id
        self.review_id = review_id