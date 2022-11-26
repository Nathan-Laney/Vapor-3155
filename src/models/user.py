from models import db

class User(db.Model): 
    __tablename__ = 'user'

    user_id =       db.Column(db.Integer, primary_key=True)
    username =      db.Column(db.String, nullable=False)
    email =         db.Column(db.String, nullable=False)
    password =      db.Column(db.String, nullable=False)
    first_name =    db.Column(db.String, nullable=False)

    def __init__(self, username, email, password, first_name) -> None:
        self.username = username
        self.email = email
        self.password = password
        self.first_name = first_name
