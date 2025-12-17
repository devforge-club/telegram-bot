from pydantic import BaseModel
from typing import Dict

class EmptyModel(BaseModel):
    pass


COMMAND_CONFIG: Dict[str, dict] = {
    # Guest commands (Everyone + Members + Admin)
    "help": {
        "roles": {"guest", "member", "admin"},
        "has_flag": False,
        "model": None,
    },
    "start": {
        "roles": {"guest", "member", "admin"},
        "has_flag": False,
        "model": None,
    },
    "about": {
        "roles": {"guest", "member", "admin"},
        "has_flag": True,
        "model": EmptyModel,
    },

    # Member commands (Members + Admin)
    "next_session": {
        "roles": {"member", "admin"},
        "has_flag": False,
        "model": None,
    },
    "confirm": {
        "roles": {"member", "admin"},
        "has_flag": True,
        "model": EmptyModel
    },
    "absent": {
        "roles": {"member", "admin"},
        "has_flag": True,
        "model": EmptyModel,
    },
    "who_comes": {
        "roles": {"member", "admin"},
        "has_flag": False,
        "model": None,
    },
    
    "resource": {
        "roles": {"member", "admin"},
        "has_flag": True,
        "model": EmptyModel,
    },
    "add_resource": {
        "roles": {"member", "admin"},
        "has_flag": True,
        "model": EmptyModel,
    },
    "recent_resources": {
        "roles": {"member", "admin"},
        "has_flag": False,
        "model": None,
    },
    "categories": {
        "roles": {"member", "admin"},
        "has_flag": False,
        "model": None,
    },
    
    "remind": {
        "roles": {"member", "admin"},
        "has_flag": True,
        "model": EmptyModel,
    },
    "reminders": {
        "roles": {"member", "admin"},
        "has_flag": False,
        "model": None,
    },
    
    "github_status": {
        "roles": {"member", "admin"},
        "has_flag": False,
        "model": None,
    },
    "my_prs": {
        "roles": {"member", "admin"},
        "has_flag": False,
        "model": None,
    },
    "my_issues": {
        "roles": {"member", "admin"},
        "has_flag": False,
        "model": None,
    },
    
    "my_profile": {
        "roles": {"member", "admin"},
        "has_flag": False,
        "model": None,
    },
    "tasks": {
        "roles": {"member", "admin"},
        "has_flag": False,
        "model": None,
    },
    "stats": {
        "roles": {"member", "admin"},
        "has_flag": False,
        "model": None,
    },
    "ranking": {
        "roles": {"member", "admin"},
        "has_flag": False,
        "model": None,
    },

    # Admin commands (Admin only)
    "summon": {
        "roles": {"admin"},
        "has_flag": True,
        "model": EmptyModel,
    },
    "promote": {
        "roles": {"admin"},
        "has_flag": True,
        "model": EmptyModel,
    },
    "demote": {
        "roles": {"admin"},
        "has_flag": True,
        "model": EmptyModel,
    },
    "member_info": {
        "roles": {"admin"},
        "has_flag": True,
        "model": EmptyModel,
    },
    "announce": {
        "roles": {"admin"},
        "has_flag": True,
        "model": EmptyModel,
    },
    "kick": {
        "roles": {"admin"},
        "has_flag": True,
        "model": EmptyModel,
    },
    "warn": {
        "roles": {"admin"},
        "has_flag": True,
        "model": EmptyModel,
    },
    "members": {
        "roles": {"admin"},
        "has_flag": False,
        "model": None,
    },
}