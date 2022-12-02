from src.models.user_data import user_data
from models import db

# credit Krevat for code inspo 

    # USER_DATA HOLDS: 
    # user_id =       db.Column(db.Integer, primary_key=True)
    # username =      db.Column(db.String, nullable=False)
    # email =         db.Column(db.String, nullable=False)
    # password =      db.Column(db.String, nullable=False)
    # first_name =    db.Column(db.String, nullable=False)

class UserRepository:

    def get_all_users(self):
        all_users: list[user_data] = user_data.query.all()
        return all_users

    def get_user_by_id(self, user_id: int) -> user_data:
        found_user: user_data = user_data.query.get_or_404(user_id)
        return found_user

    def create_user(self, username: str, email: str, password: str, first_name: str) -> user_data:
        one_user = user_data(username=username, email=email, password=password, first_name=first_name)
        db.session.add(one_user)
        db.session.commit()
        return one_user


# Singleton to be used in other modules
user_repository_singleton = UserRepository()
