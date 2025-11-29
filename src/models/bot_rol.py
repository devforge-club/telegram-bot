class BotRol:
    key: str
    name: str
    hierarchy: int
    allowed_commands: list[str]

    def __init__(self, key: str, name: str, hierarchy: int, allowed_commands: list[str]) -> None:
        self.key = key
        self.name = name
        self.hierarchy = hierarchy

        for command in allowed_commands:
            if command[0] == '/':
                raise Exception(f'Los comandos del BotRol "{key}, {name}" que se intento crear, no pueden empezar por "/", como es el caso de {command}')

        self.allowed_commands = allowed_commands
    
