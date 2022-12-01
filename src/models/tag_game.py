from models import db

# from sqlalchemy.dialects.postgresql import JSON

class tag_game(db.Model):  # type: ignore
    __tablename__ = 'tag_game'
    
    tag_id =        db.Column(db.Integer, db.ForeignKey("tag.tag_id", ondelete="CASCADE", onupdate="CASCADE"), primary_key = True)
    tag_rel = db.relationship("tag", backref = "tag_info")


    game_id =        db.Column(db.Integer, db.ForeignKey("game.game_id", ondelete="CASCADE", onupdate="CASCADE"), primary_key = True)
    game_rel = db.relationship("game", backref = "game_with_this_tag")
