def parse_command(text: str) -> list[str]:
   
    text = text.strip()
    
    if text.startswith("/"):
        text = text[1:]
        
    return text.split()