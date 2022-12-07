from src.models.review import review
from models import db
from datetime import date

# credit Krevat for code inspo 

    # REVIEW HOLDS:
    # review_id =             db.Column(db.Integer, primary_key=True)
    # date =                  db.Column(db.DateTime, nullable=False)
    # rating_score =          db.Column(db.Integer, nullable=False)
    # replayability_score =   db.Column(db.Integer, nullable=True)
    # graphics_score =        db.Column(db.Integer, nullable=True)
    # description =           db.Column(db.String, nullable=False)

class ReviewRepository:

    def get_all_reviews(self) -> list[review]:
        all_reviews: list[review] = review.query.all()
        return all_reviews

    def get_review_by_id(self, review_id: int) -> review:
        found_reviews: review = review.query.get_or_404(review_id)
        return found_reviews

    def create_review(self, date:date, rating_score:int, replayability_score:int, graphics_score:int, description:str) -> review:
        new_review = review(date=date, rating_score=rating_score, replayability_score=replayability_score, graphics_score = graphics_score, description = description)
        db.session.add(new_review)
        db.session.commit()
        return new_review

# Singleton to be used in other modules
review_repository_singleton = ReviewRepository()
