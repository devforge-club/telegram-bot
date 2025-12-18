from typing import Dict
from src.models.commands import (
    AboutCommand,
    ResourceCommand,
    AddResourceCommand,
    RemindCommand,
    SummonCommand,
    AnnounceCommand,
    WarnCommand,
)

COMMAND_CONFIG: Dict[str, dict] = {
    # Guest commands (Everyone + Members + Admin)
    "help": {
        "roles": {"guest", "member", "admin"},
        "has_flag": False,
    },
    "start": {
        "roles": {"guest", "member", "admin"},
        "has_flag": False,
    },
    "about": {
        "roles": {"guest", "member", "admin"},
        "has_flag": True,
        "model": AboutCommand,
    },

    # Member commands (Members + Admin)
    "next_session": {
        "roles": {"member", "admin"},
        "has_flag": False,
    },
    "confirm": {
        "roles": {"member", "admin"},
        "has_flag": False,
    },
    "absent": {
        "roles": {"member", "admin"},
        "has_flag": False,
    },
    "who_comes": {
        "roles": {"member", "admin"},
        "has_flag": False,
    },
    
    "resource": {
        "roles": {"member", "admin"},
        "has_flag": True,
        "model": ResourceCommand,
    },
    "add_resource": {
        "roles": {"member", "admin"},
        "has_flag": True,
        "model": AddResourceCommand,
    },
    "recent_resources": {
        "roles": {"member", "admin"},
        "has_flag": False,
    },
    "categories": {
        "roles": {"member", "admin"},
        "has_flag": False,
    },
    
    "remind": {
        "roles": {"member", "admin"},
        "has_flag": True,
        "model": RemindCommand,
    },
    "reminders": {
        "roles": {"member", "admin"},
        "has_flag": False,
    },
    
    "github_status": {
        "roles": {"member", "admin"},
        "has_flag": False,
    },
    "my_prs": {
        "roles": {"member", "admin"},
        "has_flag": False,
    },
    "my_issues": {
        "roles": {"member", "admin"},
        "has_flag": False,
    },
    
    "my_profile": {
        "roles": {"member", "admin"},
        "has_flag": False,
    },
    "tasks": {
        "roles": {"member", "admin"},
        "has_flag": False,
    },
    "stats": {
        "roles": {"member", "admin"},
        "has_flag": False,
    },
    "ranking": {
        "roles": {"member", "admin"},
        "has_flag": False,
    },

    # Admin commands (Admin only)
    "summon": {
        "roles": {"admin"},
        "has_flag": True,
        "model": SummonCommand,
    },
    "promote": {
        "roles": {"admin"},
        "has_flag": False,
    },
    "demote": {
        "roles": {"admin"},
        "has_flag": False,
    },
    "member_info": {
        "roles": {"admin"},
        "has_flag": False,
    },
    "announce": {
        "roles": {"admin"},
        "has_flag": True,
        "model": AnnounceCommand,
    },
    "kick": {
        "roles": {"admin"},
        "has_flag": False,
    },
    "warn": {
        "roles": {"admin"},
        "has_flag": True,
        "model": WarnCommand,
    },
    "members": {
        "roles": {"admin"},
        "has_flag": False,
    },
}