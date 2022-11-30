from src.models.game import Game, db

#credit Krevat for code inspo
class GameRepository:
    """Game holds title, developer, and rating"""
    # these eventually need to be changed to SQLAlchemy queries
    def __init__(self) -> None:
        self._db: list[Game] = []

    def get_all_games(self):
        game_list = Game.query.all()
        return game_list

    def get_game_by_title(self, title: str) -> Game | None:
        """Get a single game by its title or None if it does not exist"""
        game = Game.query.filter_by(title=title).first()

    def create_game(self, title: str, developer: str, rating: float) -> Game:
        """Create a new game and return it"""
        create_game = Game(game_id = game_id, title=title, publisher=publisher, description=description, developer=developer, thumbnail_link=thumbnail_link, release_date=release_date)

    def search_games(self, title):
        search_game = Game.query.filter(Game.title.ilike(f'%{title}%')).all() 
    
game_repository_singleton = GameRepository()
