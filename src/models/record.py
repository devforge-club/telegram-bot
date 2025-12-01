from dataclasses import dataclass, field
from datetime import datetime
from typing import Set, List, Optional
from src.utils.forge_rank import ForgeRank
from src.utils.formatters import int_to_roman

@dataclass
class Record:

    # Core metrics
    score: int = 0
    rank: ForgeRank = ForgeRank.ORE
    legend_level: int = 0

    # GitHub metrics
    issues_completed: int = 0
    issues_on_time: int = 0
    issues_late: int = 0
    prs_created: int = 0
    prs_merged: int = 0
    prs_rejected: int = 0
    code_reviews_done: int = 0
    projects_completed: int = 0

    # Strikes
    strikes: int = 0
    strike_history: List[dict] = field(default_factory=list)
    last_strike_date: Optional[datetime] = None
    is_in_good_standing: bool = True

    # Control & metadata
    current_projects: Set[str] = field(default_factory=set)
    last_github_sync: Optional[datetime] = None
    score_history: List[dict] = field(default_factory=list)
    rank_history: List[dict] = field(default_factory=list)

    def add_score(self, points: int, reason: str) -> dict:
        if points <= 0:
            raise ValueError(f"Points must be greater than zero, got: {points}")
        self.score += points
        old_rank = self.rank
        new_rank = ForgeRank.get_rank_by_score(self.score)
        rank_up = old_rank != new_rank
        timestamp = datetime.now()

        self.score_history.append(
            {"timestamp": timestamp, "points": points, "reason": reason}
        )

        if rank_up:
            self.rank_history.append(
                {
                    "timestamp": timestamp,
                    "old_rank": old_rank,
                    "new_rank": new_rank,
                }
            )

        self.rank = new_rank

        return {
            "rank_up": rank_up,
            "old_rank": old_rank,
            "new_rank": new_rank,
            "points_gained": points,
        }

    def add_strike(self, reason: str, details: str = "") -> None:
        self.strikes += 1
        timestamp = datetime.now()
        self.strike_history.append(
            {
                "timestamp": timestamp,
                "action": "added",
                "reason": reason,
                "details": details,
            }
        )
        self.last_strike_date = timestamp

    def remove_strike(self, reason: str, details: str = "") -> bool:
        if self.strikes > 0:
            self.strikes -= 1
            self.strike_history.append(
                {
                    "timestamp": datetime.now(),
                    "action": "removed",
                    "reason": reason,
                    "details": details,
                }
            )
            return True
        return False

    def ascend_to_legend(self) -> dict:
        success = self.score >= 4500
        old_rank = self.rank

        if success:
            self.legend_level += 1
            self.score = 0
            self.rank = ForgeRank.ORE
            self.rank_history.append(
                {
                    "timestamp": datetime.now(),
                    "old_rank": old_rank,
                    "new_rank": self.rank,
                    "legend_ascension": f"Ascended to Legend {int_to_roman(self.legend_level)}! Your journey begins anew.",
                }
            )
        message = (
            f"A legend of level {self.legend_level} was born!"
            if success
            else f"It's not time to be reborn yet, you still need to gain more experience. Actual experience points: {self.score}"
        )
        return {
            "success": success,
            "legend_level": self.legend_level,
            "previous_rank": old_rank,
            "message": message,
        }
