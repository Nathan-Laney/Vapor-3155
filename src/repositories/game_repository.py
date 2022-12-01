from src.models.game import game
from models import db
from datetime import datetime
_game_repo = None

#credit Krevat for code inspo
def get_game_repository():
    global _game_repo

    class GameRepository:
        """Game holds title, developer, and rating"""
        # these eventually need to be changed to SQLAlchemy queries
        def __init__(self) -> None:
            self._db: list[game] = []

        def get_all_games(self, games):
            return self._db

        def get_game_by_title(self, title: str) -> game | None:
            """Get a single game by its title or None if it does not exist"""
            for one_game in self._db:
                if one_game.title == title:
                    return one_game
            return None

        def create_game(self, title: str,  publisher: str, description: str, developer: str, thumbnail_link: str, release_date: datetime) -> game:
            """Create a new game and return it"""
            # (self, title: str,  publisher: str, description: str, developer: str, thumbnail_link: str, release_date: datetime)
            one_game = game(title, publisher, description, developer, thumbnail_link, release_date)
            self._db.append(one_game)
            return one_game

    if _game_repo is None:
        _game_repo = GameRepository()
    
    return _game_repo
