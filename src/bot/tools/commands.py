from aiogram.filters.command import CommandObject
from src.utils.regex import COMMAND_PARSE

def parse_command(command: CommandObject) -> dict:
    if not command.args:
        return {}
    command_list = COMMAND_PARSE.findall(command.args)
    return {k: v.strip() if v else True for k, v in command_list}
  