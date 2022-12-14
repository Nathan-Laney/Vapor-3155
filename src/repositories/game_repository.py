
from src.models.game import game
from models import db
from datetime import date
from sqlalchemy import desc, select


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

    def search_games_by_title(self, title:str) -> list[game]:
        found_games: list[game] = game.query.filter(game.title.ilike(f'%{title}%')).all()
        return found_games

    
    def get_game_by_id(self, game_id: int) -> game:
        found_game: game = game.query.get_or_404(game_id)
        return found_game

    def get_highest_rating(self):
        highest_game = []
        # sorted_games: list[game] = select(game).order_by(desc(game.rating))
        sorted_games: list[game] = db.session.query(game).order_by(desc(game.rating))
        for i in range(20):
            highest_game.append(sorted_games[i])
        return highest_game

    def create_game(self, game_id: int, title: str,  publisher: str, description: str, developer: str, thumbnail_link: str, release_date: date, rating:float) -> game:
        # (self, title: str,  publisher: str, description: str, developer: str, thumbnail_link: str, release_date: datetime)
        exists = db.session.query(game.game_id).filter_by(game_id = game_id).first()

        if (exists is not None):
            return exists
        else:
            one_game = game(game_id=game_id, title=title, publisher=publisher, description=description, developer=developer, thumbnail_link=thumbnail_link, release_date=release_date, rating=rating)
            db.session.add(one_game)
            db.session.commit()
            return one_game
    
    def create_game_without_an_id(self, title: str,  publisher: str, description: str, developer: str, thumbnail_link: str, release_date: date, rating:float) -> game:
        # (self, title: str,  publisher: str, description: str, developer: str, thumbnail_link: str, release_date: datetime)
        exists = db.session.query(game.title).filter_by(title = title).first()

        if (exists is not None):
            return exists
        else:
            one_game = game(title=title, publisher=publisher, description=description, developer=developer, thumbnail_link=thumbnail_link, release_date=release_date, rating=rating)
            db.session.add(one_game)
            db.session.commit()
            return one_game
    

# Singleton to be used in other modules
game_repository_singleton = GameRepository()
