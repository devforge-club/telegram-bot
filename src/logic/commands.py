def clean_command(command: str | list[str]):

    if type(command) is str:
        return command[1:] if command[0]=='/' else command
    
    arr = [comm[1:] if comm[0]=='/' else comm for comm in command]
    
    return arr
