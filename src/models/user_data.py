from models import db

class user_data(db.Model):   # type: ignore
    __tablename__ = 'user_data'

    user_id =       db.Column(db.Integer, primary_key=True)
    username =      db.Column(db.String, nullable=False)
    email =         db.Column(db.String, nullable=False)
    password =      db.Column(db.String, nullable=False)
    first_name =    db.Column(db.String, nullable=False)
    profile_path =  db.Column(db.String, nullable=False)

    def __init__(self, username, email, password, first_name, profile_path) -> None:
        self.username = username
        self.email = email
        self.password = password
        self.first_name = first_name
        self.profile_path = profile_path
