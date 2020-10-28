import importlib.resources
import importlib
import argparse
import sys
import os

scripts = {}
with importlib.resources.path("riskan", "scripts") as path:
    for name in os.listdir(path):
        if (
            not name.startswith("_")
            and not name.startswith(".")
            and name.endswith(".py")
        ):
            name = name[:-3]
            mod = importlib.import_module(f"riskan.scripts.{name}")
            if not hasattr(mod, "add_arguments"):
                sys.exit(
                    f"Script '{name}' does not contain a 'def add_arguments(parser)'"
                )

            if not hasattr(mod, "execute"):
                sys.exit(f"Script '{name}' does not contain a 'def execute(args)'")

            scripts[name] = mod


def main(argv=None):
    if argv is None:
        argv = sys.argv

    action = None
    if len(sys.argv) > 1:
        action = sys.argv[1]

    if action not in scripts:
        action = "help"

    parser = scripts[action].add_arguments(
        argparse.ArgumentParser(prog=f"riskan {action}")
    )
    scripts[action].execute(parser.parse_args(argv[2:]))
