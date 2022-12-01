from models import db

# from sqlalchemy.dialects.postgresql import JSON

class user_favorites(db.Model):  # type: ignore
    __tablename__ = 'user_favorites'
    
    user_id =        db.Column(db.Integer, db.ForeignKey("user_data.user_id", ondelete="CASCADE", onupdate="CASCADE"), primary_key = True)
    user_rel = db.relationship("user_data", backref = "user_data")


    game_id =        db.Column(db.Integer, db.ForeignKey("game.game_id", ondelete="CASCADE", onupdate="CASCADE"), primary_key = True)
    game_rel = db.relationship("game", backref = "game")
