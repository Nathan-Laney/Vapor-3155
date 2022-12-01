from src.models.tag import tag
from models import db


class tagRepository:

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

    def search_tags(self, title) -> list[tag]:
        found_tags: list[tag] = tag.query.filter(tag.title.ilike(f'%{title}%')).all()
        return found_tags


# Singleton to be used in other modules
tag_repository_singleton = tagRepository()
