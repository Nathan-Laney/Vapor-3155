from models import db
# from sqlalchemy.dialects.postgresql import JSON

class tag(db.Model):  # type: ignore
    __tablename__ = 'tag'
    
    tag_id =            db.Column(db.Integer, primary_key=True)
    tag_description =   db.Column(db.String, nullable=True)

    # tag_game = db.relationship("tag_game", cascade="all,delete", backref="tag")

    def __init__(self, tag_description:str) -> None:
        self.tag_description = tag_description
