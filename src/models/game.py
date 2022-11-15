class Game:
    """Game holds title, developer, and rating"""

    def __init__(self, title: str, developer: str, rating: float) -> None:
        self.title = title
        self.developer = developer
        self.rating = rating