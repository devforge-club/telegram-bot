COMMAND_ALLOWLIST = {
    # Comandos de Guest (Todos + Miembros + Admin)
    "ayuda": ["everyone", "member", "admin"],
    "start": ["everyone", "member", "admin"],
    "sobre": ["everyone", "member", "admin"],

    # Comandos de Member (Miembros + Admin)
    "proxima_sesion": ["member", "admin"],
    "confirmar": ["member", "admin"],
    "ausente": ["member", "admin"],
    "quien_viene": ["member", "admin"],
    "recurso": ["member", "admin"],
    "agregar_recurso": ["member", "admin"],
    "recursos_recientes": ["member", "admin"],
    "categorias": ["member", "admin"],
    "recordar": ["member", "admin"],
    "recordatorios": ["member", "admin"],
    "github_status": ["member", "admin"],
    "mis_prs": ["member", "admin"],
    "mis_issues": ["member", "admin"],
    "mi_perfil": ["member", "admin"],
    "tareas": ["member", "admin"],
    "stats": ["member", "admin"],
    "ranking": ["member", "admin"],

    # Comandos de Admin (Solo Admin)
    "convocar": ["admin"],
    "promover": ["admin"],
    "degradar": ["admin"],
    "info_member": ["admin"],
    "anuncio": ["admin"],
    "expulsar": ["admin"],
    "warn": ["admin"],
    "miembros": ["admin"]
}