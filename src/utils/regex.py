import re

COMMAND_PARSE = re.compile(r"--([^\s]+)(?:\s+((?:(?!--).)*))?(?=\s*--|$)")
