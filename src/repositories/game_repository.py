from src.models.game import game 
from models import db

class GameRepository:

    def get_all_games(self):
        game_list = game.query.all()
        return game_list

    def get_game_by_title(self, title):
        game = game.query.filter_by(title=title).first()

    def create_game(self, game_id, title, publisher, description, developer, thumbnail_link, release_date):
        create_game = game(game_id = game_id, title=title, publisher=publisher, description=description, developer=developer, thumbnail_link=thumbnail_link, release_date=release_date)
        db.session.add(create_game)
        db.session.commit()
        return create_game

    def search_games(self, title):
        search_game = game.query.filter(game.title.ilike(f'%{title}%')).all() 
    
game_repository_singleton = GameRepository