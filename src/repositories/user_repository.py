from src.models.user_data import user_data
_user_repo = None

#credit Krevat for code inspo
def get_user_repository():
    global _user_repo

    class GameRepository:
        """Game holds title, developer, and rating"""
        # these eventually need to be changed to SQLAlchemy queries
        def __init__(self) -> None:
            self._db: list[user_data] = []

        def get_all_users(self, users):
            return self._db

        def get_user_by_title(self, title: str) -> user_data | None:
            """Get a single user by its title or None if it does not exist"""
            for one_user in self._db:
                if one_user.title == title:
                    return one_user
            return None

        def create_user(self, username:str, email:str, password:str, first_name:str) -> user_data:
            """Create a new user and return it"""
            # (self, title: str,  publisher: str, description: str, developer: str, thumbnail_link: str, release_date: datetime)
            one_user = user_data(username, email, password, first_name)
            self._db.append(one_user)
            return one_user

    if _user_repo is None:
        _user_repo = GameRepository()
    
    return _user_repo
