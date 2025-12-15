from pydantic import BaseModel, Field

from datetime import datetime

from src.utils.forge_rank import ForgeRank
from src.utils.formatters import int_to_roman
from src.models.score_logs import ScoreLog

LEGEND_ASCENSION_THRESHOLD = 4500
MAX_STRIKES_ALLOWED = 3


class StrikeEntry(BaseModel):
    timestamp: datetime
    action: str
    reason: str
    details: str


class RankEntry(BaseModel):
    timestamp: datetime
    old_rank: str
    new_rank: str
    legend_ascension: str | None = None


class Record(BaseModel):

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
    projects_completed: set[str] = Field(default_factory=set)

    # Strikes
    strikes: int = 0
    strike_history: list[StrikeEntry] = Field(default_factory=list)
    last_strike_date: datetime | None = None

    # Control & metadata
    current_projects: set[str] = Field(default_factory=set)
    last_github_sync: datetime | None = None
    rank_history: list[RankEntry] = Field(default_factory=list)

    def add_score(self, score_log: ScoreLog) -> dict:
        self.score += score_log.points
        old_rank = self.rank
        new_rank = ForgeRank.get_rank_by_score(self.score)
        rank_up = old_rank != new_rank

        if rank_up:
            self.rank_history.append(
                RankEntry(
                    **{
                        "timestamp": score_log.timestamp,
                        "old_rank": old_rank.display_name,
                        "new_rank": new_rank.display_name,
                    }
                )
            )

        self.rank = new_rank

        return {
            "rank_up": rank_up,
            "old_rank": old_rank.display_name,
            "new_rank": new_rank.display_name,
            "points_gained": score_log.points,
        }

    def add_strike(self, reason: str, details: str = "") -> None:
        if not reason or not reason.strip():
            raise ValueError("Reason for strike must be provided")
        self.strikes += 1
        timestamp = datetime.now()
        self.strike_history.append(
            StrikeEntry(
                **{
                    "timestamp": timestamp,
                    "action": "added",
                    "reason": reason,
                    "details": details,
                }
            )
        )
        self.last_strike_date = timestamp

    def remove_strike(self, reason: str, details: str = "") -> bool:
        if not reason or not reason.strip():
            raise ValueError("Reason for strike removal must be provided")
        if self.strikes > 0:
            self.strikes -= 1
            self.strike_history.append(
                StrikeEntry(
                    **{
                        "timestamp": datetime.now(),
                        "action": "removed",
                        "reason": reason,
                        "details": details,
                    }
                )
            )
            return True
        return False

    def ascend_to_legend(self) -> dict[str, object]:
        success = self.score >= LEGEND_ASCENSION_THRESHOLD
        old_rank = self.rank

        if success:
            self.legend_level += 1
            self.score = 0
            self.rank = ForgeRank.ORE
            self.rank_history.append(
                RankEntry(
                    **{
                        "timestamp": datetime.now(),
                        "old_rank": old_rank.display_name,
                        "new_rank": self.rank.display_name,
                        "legend_ascension": f"Ascended to Legend {int_to_roman(self.legend_level)}! Your journey begins anew.",
                    }
                )
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

    def get_progress_to_next_rank(self) -> dict:
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

    def inc_issues_completed(self) -> None:
        self.issues_completed += 1

    def inc_issues_on_time(self) -> None:
        self.issues_on_time += 1

    def inc_issues_late(self) -> None:
        self.issues_late += 1

    def inc_prs_created(self) -> None:
        self.prs_created += 1

    def inc_prs_merged(self) -> None:
        self.prs_merged += 1

    def inc_prs_rejected(self) -> None:
        self.prs_rejected += 1

    def inc_code_reviews(self) -> None:
        self.code_reviews_done += 1

    def add_project(self, project_url: str) -> None:
        self.current_projects.add(project_url)

    def remove_project(self, project_url: str) -> None:
        self.current_projects.discard(project_url)

    def complete_project(self, project_url: str) -> None:
        self.remove_project(project_url)
        self.projects_completed.add(project_url)

    def is_working_on_project(self, project_url: str) -> bool:
        return project_url in self.current_projects

    @property
    def completion_rate(self) -> float:
        return (
            0.0
            if self.issues_completed == 0
            else float(self.issues_on_time) / self.issues_completed
        )

    @property
    def pr_approval_rate(self) -> float:
        return (
            0.0 if self.prs_created == 0 else float(self.prs_merged) / self.prs_created
        )

    @property
    def is_in_good_standing(self) -> bool:
        return self.strikes < MAX_STRIKES_ALLOWED

    @property
    def legend_badge(self) -> str | None:
        if self.legend_level == 0:
            return None

        return f"Legend {int_to_roman(self.legend_level)}"

    @property
    def display_rank(self) -> str:
        rank = self.rank.display_name
        if self.legend_level > 0:
            rank = f"{self.legend_badge} • {rank}"
        return rank

    def get_stats_summary(self) -> dict:
        return {
            "rank": self.display_rank,
            "score": self.score,
            "legend_level": self.legend_level,
            "strikes": self.strikes,
            "is_in_good_standing": self.is_in_good_standing,
            "contributions": {
                "issues_completed": self.issues_completed,
                "issues_on_time": self.issues_on_time,
                "issues_late": self.issues_late,
                "prs_merged": self.prs_merged,
                "code_reviews": self.code_reviews_done,
                "count_projects_completed": len(self.projects_completed),
            },
            "rates": {
                "completion_rate": self.completion_rate,
                "pr_approval_rate": self.pr_approval_rate,
            },
            "count_current_projects": len(self.current_projects),
        }

    def __str__(self) -> str:
        return (
            f"Rank: {self.display_rank}, Score: {self.score}, Strikes: {self.strikes})"
        )
