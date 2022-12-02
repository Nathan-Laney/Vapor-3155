from src.models.game import game
from models import db
from datetime import datetime


# credit Krevat for code inspo

    # GAME HOLDS: 
    # game_id =           db.Column(db.Integer, primary_key=True)
    # title =             db.Column(db.String, nullable=False)
    # publisher =         db.Column(db.String, nullable=True)
    # description =       db.Column(db.String, nullable=True)
    # developer =         db.Column(db.String, nullable=True)
    # thumbnail_link =    db.Column(db.String, nullable=True)
    # release_date =      db.Column(db.DateTime, nullable=False)


class GameRepository:
    def get_all_games(self):
        all_games: list[game] = game.query.all()
        return all_games

    def search_games_by_title(self, title) -> list[game]:
        found_games: list[game] = game.query.filter(game.title.ilike(f'%{title}%')).all()
        return found_games

    def create_game(self, game_id: int, title: str,  publisher: str, description: str, developer: str, thumbnail_link: str, release_date: datetime) -> game:
        # (self, title: str,  publisher: str, description: str, developer: str, thumbnail_link: str, release_date: datetime)
        one_game = game(game_id, title, publisher, description, developer, thumbnail_link, release_date)
        db.append(one_game)
        return one_game

# Singleton to be used in other modules
game_repository_singleton = GameRepository()
