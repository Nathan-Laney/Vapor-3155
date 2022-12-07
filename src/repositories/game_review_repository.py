from src.models.game_review import game_review
from models import db

# credit Krevat for code inspo 

    # game_review HOLDS:
    # review_id = db.Column(db.Integer, db.ForeignKey("review.review_id", ondelete="CASCADE", onupdate="CASCADE"), primary_key = True)
    # review_rel = db.relationship("review", backref = "review")
    # game_id = db.Column(db.Integer, db.ForeignKey("game.game_id", ondelete="CASCADE", onupdate="CASCADE"), primary_key = True)
    # game_rel = db.relationship("game", backref = "game")



class GameReviewRepository:

    def get_all_game_reviews(self):
        all_game_reviews: list[game_review] = game_review.query.all()
        return all_game_reviews

    def game_reviews_by_review_id(self, review_id: int) -> game_review:
        matches: game_review = game_review.query.get_or_404(review_id)
        return matches

    def game_reviews_by_game_id(self, game_id: int) -> game_review:
        matches: game_review = game_review.query.get_or_404(game_id)
        return matches

    def create_game_review(self, review_id:int, game_id:int) -> game_review:
        exists = db.session.query(game_review.review_id).filter_by(review_id = review_id, game_id = game_id).first()

        if (exists is not None):
            return exists
        else:
            created_review = game_review(review_id=review_id, game_id=game_id)
            db.session.add(created_review)
            db.session.commit()
            return created_review

# Singleton to be used in other modules
game_review_repository_singleton = GameReviewRepository()
