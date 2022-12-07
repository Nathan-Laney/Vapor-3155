from models import db

class user_data(db.Model):   # type: ignore
    __tablename__ = 'user_data'

    user_id =       db.Column(db.Integer, primary_key=True)
    username =      db.Column(db.String, nullable=False)
    email =         db.Column(db.String, nullable=False)
    password =      db.Column(db.String, nullable=False)
    first_name =    db.Column(db.String, nullable=False)
    profile_path =  db.Column(db.String, nullable=False)
    