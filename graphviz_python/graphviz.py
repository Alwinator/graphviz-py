import os
import shlex
import shutil
import logging
from typing import List


def execute_graphviz(graphviz_code: str, arguments: List[str]) -> str:
    """
    Executes a graphviz command
    """
    executable = shutil.which('dot') or shutil.which('graphviz')

    if not executable:
        raise ModuleNotFoundError(f'graphviz / dot executable not found! '
                                  f'Please install graphviz and make sure you have it in the PATH variable.')

    arg = " ".join(arguments)
    cmd = f'echo {shlex.quote(graphviz_code)} | {executable} {arg}'
    logging.debug(f"Executing in command line: {cmd}")
    os.system(cmd)

