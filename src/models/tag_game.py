from models import db

# from sqlalchemy.dialects.postgresql import JSON

class tag_game(db.Model):  # type: ignore
    __tablename__ = 'tag_game'
    
    tag_id =        db.Column(db.Integer, db.ForeignKey("tag.tag_id", ondelete="CASCADE", onupdate="CASCADE"), primary_key = True)
    tag_rel = db.relationship("tag", backref = "tag")


    game_id =        db.Column(db.Integer, db.ForeignKey("game.game_id", ondelete="CASCADE", onupdate="CASCADE"), primary_key = True)
    game_rel = db.relationship("game", backref = "game")

    def __init__(self, tag_id:int, game_id:int) -> None:
        self.tag_id = tag_id
        self.game_id = game_id