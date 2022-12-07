from src.models.tag_game import tag_game
from models import db

# credit Krevat for code inspo 

    # tag_game HOLDS:
    # tag_id = db.Column(db.Integer, db.ForeignKey("tag.tag_id", ondelete="CASCADE", onupdate="CASCADE"), primary_key = True)
    # tag_rel = db.relationship("tag", backref = "tag_info")
    # game_id = db.Column(db.Integer, db.ForeignKey("game.game_id", ondelete="CASCADE", onupdate="CASCADE"), primary_key = True)
    # game_rel = db.relationship("game", backref = "game_with_this_tag")


class TagGameRepository:

    def get_all_tag_games(self):
        all_tag_games: list[tag_game] = tag_game.query.all()
        return all_tag_games

    def tag_games_by_review_id(self, review_id: int) -> tag_game:
        matches: tag_game = tag_game.query.get_or_404(review_id)
        return matches

    def tag_games_by_game_id(self, game_id: int) -> tag_game:
        matches: tag_game = tag_game.query.get_or_404(game_id)
        return matches

    def create_tag_game(self, tag_id:int, game_id:int) -> tag_game:
        created_review = tag_game(tag_id=tag_id, game_id=game_id)
        db.session.add(created_review)
        db.session.commit()
        return created_review

# Singleton to be used in other modules
tag_game_repository_singleton = TagGameRepository()
