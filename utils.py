import os
import textwrap

from display import DIM, RESET, _c, _use_color

DEBUG = os.getenv("DEBUG", "false").lower() == "true"


def debug(message, prefix="DEBUG"):
    """
    Verbose debug — only when DEBUG=true in .env
    Shows raw LLM output, iterations, full state snippets.
    """
    if not DEBUG:
        return

    label = _c(f"[{prefix}]", "\033[38;5;108m") if _use_color() else f"[{prefix}]"
    text = str(message)
    if "\n" in text:
        print(f"    {label}")
        for line in text.splitlines():
            wrapped = textwrap.wrap(line, width=68) or [""]
            for w in wrapped:
                print(f"      {_c(w, DIM)}{RESET if _use_color() else ''}")
    else:
        wrapped = textwrap.wrap(text, width=68) or [text]
        for i, w in enumerate(wrapped):
            if i == 0:
                print(f"    {label} {w}")
            else:
                print(f"         {w}")
