import uuid
from datetime import datetime
from typing import Dict, List, Any, Self
from enum import Enum
from src.utils.issue_difficulty import IssueDifficulty


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


class Task:
    id: str
    title: str
    description: str | None
    task_type: TaskType
    assigned_to: str
    created_by: str
    project_url: str | None
    github_url: str | None
    github_task_number: str | None
    difficulty: IssueDifficulty
    points_reward: int
    status: TaskStatus
    due_date: datetime | None
    created_at: datetime
    started_at: datetime | None
    completed_at: datetime | None
    notes: List[Dict[str, Any]] | None

    def __init__(
        self,
        title: str,
        assigned_to: str,
        created_by: str,
        difficulty: IssueDifficulty,
        task_type: TaskType = TaskType.CUSTOM,
        description: str | None = None,
        project_url: str | None = None,
        github_url: str | None = None,
        github_task_number: int | None = None,
        due_date: datetime | None = None,
        created_at: datetime | None = None,
        status: TaskStatus = TaskStatus.PENDING,
        started_at: datetime | None = None,
        completed_at: datetime | None = None,
        notes: List[Dict] | None = None,
        task_id: str | None = None,
    ):
        # informacion basica
        self.id = task_id or str(uuid.uuid4())
        self.title = title
        self.description = description
        self.task_type = task_type
        # Asigancion
        self.assigned_to = assigned_to
        self.created_by = created_by
        self.project_url = project_url
        # Github
        self.github_url = github_url
        self.github_task_number = github_task_number
        # Dificultad y puntos
        self.difficulty = difficulty
        self.points_reward = difficulty.points
        # Fechas y estado
        self.status = status
        self.due_date = due_date
        self.created_at = created_at or datetime.now()
        self.started_at = started_at
        self.completed_at = completed_at
        # Metadata
        self.notes = notes or []

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

    def to_dict(self) -> Dict[str, Any]:
        """Serializa la tarea a diccionario para guardar en BD"""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "task_type": self.task_type.value,
            "assigned_to": self.assigned_to,
            "created_by": self.created_by,
            "project_url": self.project_url,
            "github_url": self.github_url,
            "github_task_number": self.github_task_number,
            "difficulty": self.difficulty.display_name,
            "points_reward": self.points_reward,
            "status": self.status.value,
            "due_date": self.due_date.isoformat() if self.due_date else None,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "started_at": self.started_at.isoformat() if self.started_at else None,
            "completed_at": (
                self.completed_at.isoformat() if self.completed_at else None
            ),
            "notes": self.notes,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Self:
        """Crea una instancia de Task desde un diccionario"""
        data_due_date = None
        if data.get("due_date"):
            data_due_date = datetime.fromisoformat(data["due_date"])

        data_created_at = None
        if data.get("created_at"):
            data_created_at = datetime.fromisoformat(data["created_at"])

        data_started_at = None
        if data.get("started_at"):
            data_started_at = datetime.fromisoformat(data["started_at"])

        data_completed_at = None
        if data.get("completed_at"):
            data_completed_at = datetime.fromisoformat(data["completed_at"])

        return cls(
            title=data["title"],
            assigned_to=data["assigned_to"],
            created_by=data["created_by"],
            difficulty=IssueDifficulty.get_difficulty_by_name(data["difficulty"]),
            task_type=TaskType(data.get("task_type", "CUSTOM")),
            description=data.get("description"),
            project_url=data.get("project_url"),
            github_url=data.get("github_url"),
            github_task_number=data.get("github_task_number"),
            due_date=data_due_date,
            created_at=data_created_at,
            status=TaskStatus(data.get("status", "PENDING")),
            started_at=data_started_at,
            completed_at=data_completed_at,
            notes=data.get("notes", []),
            task_id=data["id"],
        )
