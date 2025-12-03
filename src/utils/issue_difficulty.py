from enum import Enum


class IssueDifficulty(Enum):
    TRIVIAL = (10, "trivial")
    EASY = (25, "easy")
    MEDIUM = (50, "medium")
    HARD = (100, "hard")
    EPIC = (200, "epic")

    def __init__(self, points: int, display_name: str):
        self.points = points
        self.display_name = display_name
