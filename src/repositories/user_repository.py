from src.models.user_data import user_data
from models import db

# credit Krevat for code inspo 

    # USER_DATA HOLDS: 
    # user_id =       db.Column(db.Integer, primary_key=True)
    # username =      db.Column(db.String, nullable=False)
    # email =         db.Column(db.String, nullable=False)
    # password =      db.Column(db.String, nullable=False)
    # first_name =    db.Column(db.String, nullable=False)
    # profile_path =  db.Column(db.String, nullable=False)

class UserRepository:

    def get_all_users(self):
        all_users: list[user_data] = user_data.query.all()
        return all_users

    def get_user_by_id(self, user_id: int) -> user_data:
        found_user: user_data = user_data.query.get_or_404(user_id)
        return found_user

    def get_user_by_email(self, email: str) -> user_data:
        found_user: user_data = user_data.query.filter_by(email=email).first()
        return found_user

    def create_user(self, username: str, email: str, password: str, first_name: str, profile_path:str) -> user_data: 
        exists = db.session.query(user_data.user_id).filter_by(email = email).first()
        if (exists is not None):
            return exists
        else:
            one_user = user_data(username=username, email=email, password=password, first_name=first_name, profile_path=profile_path)
            db.session.add(one_user)
            db.session.commit()
            return one_user

    def delete_user(self, user_id: int): 
        found_user: user_data = user_data.query.get_or_404(user_id)
        db.session.delete(user_data)
        db.session.commit()
        return True

# Singleton to be used in other modules
user_repository_singleton = UserRepository()
