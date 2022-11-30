from src.models.game import Game

# _game_repo = None

#credit Krevat for code inspo
class GameRepository:
    """Game holds title, developer, and rating"""
    # these eventually need to be changed to SQLAlchemy queries
    def __init__(self) -> None:
        self._db: list[Game] = []

    def get_all_games(self, games):
        return self._db

    def get_game_by_title(self, title: str) -> Game | None:
        """Get a single game by its title or None if it does not exist"""
        for game in self._db:
            if game.title == title:
                return game
        return None

    def create_game(self, title: str, developer: str, rating: float) -> Game:
        """Create a new game and return it"""
        game = Game(title, developer, rating)
        self._db.append(game)
        return game

    def get_game_by_id(self, game_id):
        game_by_id = Game.query.filter_by(game_id=game_id).first()
        return game_by_id
    
# if _game_repo is None:
#     _game_repo = GameRepository()

game_repository = GameRepository()
