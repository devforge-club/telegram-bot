COMMAND_CONFIG = {
    # Guest commands (Everyone + Members + Admin)
    "help": {"guest", "member", "admin"},
    "start": {"guest", "member", "admin"},
    "about": {"guest", "member", "admin"},

    # Member commands (Members + Admin)
    "next_session": {"member", "admin"},
    "confirm": {"member", "admin"},
    "absent": {"member", "admin"},
    "who_comes": {"member", "admin"},
    
    "resource": {"member", "admin"},
    "add_resource": {"member", "admin"},
    "recent_resources": {"member", "admin"},
    "categories": {"member", "admin"},
    
    "remind": {"member", "admin"},
    "reminders": {"member", "admin"},
    
    "github_status": {"member", "admin"},
    "my_prs": {"member", "admin"},
    "my_issues": {"member", "admin"},
    
    "my_profile": {"member", "admin"},
    "tasks": {"member", "admin"},
    "stats": {"member", "admin"},
    "ranking": {"member", "admin"},

    # Admin commands (Admin only)
    "summon": {"admin"},
    "promote": {"admin"},
    "demote": {"admin"},
    "member_info": {"admin"},
    "announce": {"admin"},
    "kick": {"admin"},
    "warn": {"admin"},
    "members": {"admin"}
}