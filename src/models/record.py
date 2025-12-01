from dataclasses import dataclass, field
from datetime import datetime
from typing import Set, List, Optional, Self, Dict, Any
from src.utils.forge_rank import ForgeRank
from src.utils.formatters import int_to_roman

LEGEND_ASCENSION_THRESHOLD = 4500


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
    last_strike_date: datetime | None = None
    is_in_good_standing: bool = True

    # Control & metadata
    current_projects: Set[str] = field(default_factory=set)
    last_github_sync: datetime | None = None
    score_history: List[dict] = field(default_factory=list)
    rank_history: List[dict] = field(default_factory=list)

    def add_score(self, points: int, reason: str) -> Dict[str, Any]:
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
                    "old_rank": old_rank.display_name,
                    "new_rank": new_rank.display_name,
                }
            )

        self.rank = new_rank

        return {
            "rank_up": rank_up,
            "old_rank": old_rank.display_name,
            "new_rank": new_rank.display_name,
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
        if self.strikes > 3:
            self.is_in_good_standing = False

    def remove_strike(self, reason: str, details: str = "") -> bool:
        if self.strikes > 0:
            self.strikes -= 1
            if self.strikes < 3:
                self.is_in_good_standing = True
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

    def ascend_to_legend(self) -> Dict[str, Any]:
        success = self.score >= LEGEND_ASCENSION_THRESHOLD
        old_rank = self.rank

        if success:
            self.legend_level += 1
            self.score = 0
            self.rank = ForgeRank.ORE
            self.rank_history.append(
                {
                    "timestamp": datetime.now(),
                    "old_rank": old_rank.display_name,
                    "new_rank": self.rank.display_name,
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
            "previous_rank": old_rank.display_name,
            "message": message,
        }

    def get_progress_to_next_rank(self) -> Dict[str, Any]:
        next_rank = ForgeRank.get_next_rank(self.rank)
        if next_rank is None:
            progress_percentage = 100.0
            points_needed = 0
            next_rank_name = None
        else:
            points_in_current = self.score - self.rank.min_score
            segment_size = next_rank.min_score - self.rank.min_score
            progress_percentage = (points_in_current / segment_size) * 100.0
            points_needed = next_rank.min_score - self.score
            next_rank_name = next_rank.display_name

        return {
            "current_rank": self.rank.display_name,
            "next_rank": next_rank_name,
            "progress_percentage": round(progress_percentage, 2),
            "points_needed": max(0, points_needed),
            "current_score": self.score,
            "legend_eligible": self.score >= LEGEND_ASCENSION_THRESHOLD,
        }
