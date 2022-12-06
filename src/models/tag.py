
from models import db
# from sqlalchemy.dialects.postgresql import JSON

class tag(db.Model):  # type: ignore
    __tablename__ = 'tag'
    tag_id =            db.Column(db.Integer, primary_key=True)
    tag_description =   db.Column(db.String, nullable=True)
