from enum import Enum
from typing import Self


class ForgeRank(Enum):
    ORE = (1, "Ore", 0)
    COPPER = (2, "Copper", 200)
    SILVER = (3, "Silver", 400)
    GOLD = (4, "Gold", 600)
    PLATINUM = (5, "Platinum", 800)
    MYTHRIL = (6, "Mythril", 1000)
    ORICHALCUM = (7, "Orichalcum", 1300)
    DRAGONSTEEL = (8, "Dragonsteel", 1650)
    FORGELORD_I = (9, "Forgelord I", 2000)
    FORGELORD_II = (10, "Forgelord II", 2500)
    FORGELORD_III = (11, "Forgelord III", 3000)
    FORGELORD_IV = (12, "Forgelord IV", 3500)
    MASTER_ETERNAL = (13, "Master of Eternal Forge", 4000)

    def __init__(self, level: int, display_name: str, min_score: int):
        self.level = level
        self.display_name = display_name
        self.min_score = min_score

    @classmethod
    def get_rank_by_score(cls, score: int) -> Self:
        sorted_ranks = sorted(list(cls), key=lambda r: r.min_score, reverse=True)
        for rank in sorted_ranks:
            if score >= rank.min_score:
                return rank
        return cls['ORE']

    @classmethod
    def get_rank_by_display_name(cls, name: str) -> Self | None:
        for rank in cls:
            if rank.display_name == name:
                return rank
        return None

    @classmethod
    def get_next_rank(cls, current_rank: Self) -> Self | None:
        for rank in cls:
            if current_rank.level + 1 == rank.level:
                return rank
        return None
