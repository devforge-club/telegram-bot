import uuid
from datetime import datetime
from typing import Dict, List, Any, Self
from enum import Enum
from src.utils.issue_difficulty import IssueDifficulty
from pydantic import BaseModel, Field


class TaskType(Enum):
    CUSTOM = "CUSTOM"
    ISSUE = "ISSUE"
    PULL_REQUEST = "PULL_REQUEST"
    REVIEW = "REVIEW"
    DOCUMENTATION = "DOCUMENTATION"


class TaskStatus(Enum):
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"
    OVERDUE = "OVERDUE"


class Task(BaseModel):
    # informacion basica
    id: str = Field(min_length=1, max_length=12)
    title: str = Field(min_length=4, max_length = 40)
    description: str = Field(min_length=8, max_length=256, default=None)
    task_type: TaskType
    # Asigancion
    assigned_to: str = Field(min_length=1)
    created_by: str = Field(min_length=1)
    project_url: str = Field(min_length=1, default=None)
    # Github
    github_url: str = Field(min_length=1, default=None)
    github_task_number: str = Field(min_length=1, default=None)
    # Dificultad y puntos
    difficulty: IssueDifficulty
    points_reward: int = Field(gt=0)
    # Fechas y estado
    status: TaskStatus
    due_date: datetime | None 
    created_at: datetime
    started_at: datetime | None
    completed_at: datetime | None
    # Metadata
    notes: List[Dict[str, Any]] | None

    def __str__(self) -> str:
        return f"[{self.difficulty.display_name} ~ {self.status.value}] {self.title}"

    def start(self) -> bool:
        if self.status == TaskStatus.PENDING:
            self.status = TaskStatus.IN_PROGRESS
            self.started_at = datetime.now()
            return True
        return False

    def complete(self) -> Dict[str, Any]:
        """Completa la tarea y retorna información sobre la completación"""

        success = (
            True
            if self.status not in [TaskStatus.COMPLETED, TaskStatus.CANCELLED]
            else False
        )
        if success:
            self.status = TaskStatus.COMPLETED
            self.completed_at = datetime.now()
        return {
            "success": success,
            "was_on_time": (
                True if self.due_date and self.completed_at <= self.due_date else False
            ),
            "points_earned": self.points_reward if success else 0,
            "task_type": self.task_type,
        }

    def cancel(self, reason: str = "") -> bool:
        """Cancela la tarea con una razón opcional"""
        if self.status in [TaskStatus.COMPLETED, TaskStatus.CANCELLED]:
            return False

        self.status = TaskStatus.CANCELLED
        if reason:
            self.add_note(f"Tarea cancelada: {reason}")
        return True

    def is_overdue(self) -> bool:
        """Verifica si la tarea está vencida"""
        if not self.due_date:
            return False

        if self.status in [TaskStatus.COMPLETED, TaskStatus.CANCELLED]:
            return False

        return datetime.now() > self.due_date

    def update_status_if_overdue(self) -> bool:
        """Actualiza el estado a OVERDUE si corresponde"""
        if self.is_overdue():
            self.status = TaskStatus.OVERDUE
            return True
        return False

    def get_time_remaining(self) -> Dict[str, Any]:
        """Calcula el tiempo restante hasta la fecha límite"""
        if not self.due_date:
            return {
                "has_deadline": False,
                "is_overdue": None,
                "days": None,
                "hours": None,
                "human_readable": "Sin fecha límite",
            }

        now = datetime.now()
        difference = self.due_date - now
        is_overdue = difference.total_seconds() < 0

        # Calcular días y horas
        total_seconds = abs(difference.total_seconds())
        days = int(total_seconds // 86400)
        hours = int((total_seconds % 86400) // 3600)

        # Crear mensaje legible
        if is_overdue:
            if days > 0:
                human_readable = f"Vencida hace {days} día{'s' if days != 1 else ''}"
                if hours > 0:
                    human_readable += f", {hours} hora{'s' if hours != 1 else ''}"
            else:
                human_readable = f"Vencida hace {hours} hora{'s' if hours != 1 else ''}"
        else:
            if days > 0:
                human_readable = f"{days} día{'s' if days != 1 else ''}"
                if hours > 0:
                    human_readable += f", {hours} hora{'s' if hours != 1 else ''}"
            else:
                human_readable = f"{hours} hora{'s' if hours != 1 else ''}"

        return {
            "has_deadline": True,
            "is_overdue": is_overdue,
            "days": days,
            "hours": hours,
            "human_readable": human_readable,
        }

    def add_note(self, note: str) -> None:
        """Añade una nota con timestamp a la tarea"""
        if self.notes is None:
            self.notes = []

        self.notes.append({"date": datetime.now().isoformat(), "content": note})

    # Propiedades calculadas
    @property
    def is_completed(self) -> bool:
        """Verifica si la tarea está completada"""
        return self.status == TaskStatus.COMPLETED

    @property
    def is_active(self) -> bool:
        """Verifica si la tarea está activa (pending o in progress)"""
        return self.status in [TaskStatus.PENDING, TaskStatus.IN_PROGRESS]

    @property
    def days_since_created(self) -> int:
        """Calcula días desde que se creó la tarea"""
        delta = datetime.now() - self.created_at
        return delta.days
