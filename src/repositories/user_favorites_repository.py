from src.models.user_favorites import user_favorites
from models import db

# credit Krevat for code inspo 

    # USER_FAVORITES HOLDS:
    # user_id = db.Column(db.Integer, db.ForeignKey("user_data.user_id", ondelete="CASCADE", onupdate="CASCADE"), primary_key = True)
    # user_rel = db.relationship("user_data", backref = "user_data")
    # game_id = db.Column(db.Integer, db.ForeignKey("game.game_id", ondelete="CASCADE", onupdate="CASCADE"), primary_key = True)
    # game_rel = db.relationship("game", backref = "game")


class UserFavoritesRepository:

    def get_all_user_favorites(self):
        all_user_favorites: list[user_favorites] = user_favorites.query.all()
        return all_user_favorites

    def user_favorites_by_user_id(self, user_id: int) -> user_favorites:
        matches: user_favorites = user_favorites.query.get_or_404(user_id)
        return matches

    def user_favorites_by_game_id(self, game_id: int) -> user_favorites:
        matches: user_favorites = user_favorites.query.get_or_404(game_id)
        return matches

    def create_user_favorite(self, user_id:int, game_id:int) -> user_favorites:
        exists = db.session.query(user_favorites.game_id).filter_by(user_id = user_id, game_id = game_id).first()
        if (exists is not None):
            return exists
        else:
            one_user = user_favorites(user_id=user_id, game_id=game_id)
            db.session.add(one_user)
            db.session.commit()
            return one_user

# Singleton to be used in other modules
user_favorites_repository_singleton = UserFavoritesRepository()
