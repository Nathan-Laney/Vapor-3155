from src.models.tag import tag
from models import db

# credit Krevat for code inspo 

    # TAG HOLDS:
    # tag_id =            db.Column(db.Integer, primary_key=True)
    # tag_description =   db.Column(db.String, nullable=True)

class TagRepository:

    def get_all_tags(self) -> list[tag]:
        all_tags: list[tag] = tag.query.all()
        return all_tags

    def get_tag_by_id(self, tag_id: int) -> tag:
        found_tag: tag = tag.query.get_or_404(tag_id)
        return found_tag

    def create_tag(self, tag_description:str) -> tag:
        new_tag = tag(tag_description=tag_description)
        db.session.add(new_tag)
        db.session.commit()
        return new_tag

    def search_tag_by_description(self, title:str) -> list[tag]:
        found_tags: list[tag] = tag.query.filter(tag.tag_description.ilike(f'%{title}%')).all()
        return found_tags


# Singleton to be used in other modules
tag_repository_singleton = TagRepository()
