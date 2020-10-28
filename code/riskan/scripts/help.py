"""
List what actions are available
"""

from textwrap import dedent


def add_arguments(parser):
    return parser


def execute(args):
    from riskan.executor import scripts

    actions = []

    for name, mod in scripts.items():
        actions.append(f"{name}:")
        actions.append(len(f"{name}:") * "-")
        if mod.__doc__:
            for line in mod.__doc__.split("\n"):
                actions.append(f"    {line}")
        actions.append("\n")

    actions = "\n".join(actions).strip()

    print(
        dedent(
            f"""
    To run a script, use `riskan <action> --argument1 value --argument2 value2`

    You may choose an action from:

{actions}
    """
        )
    )
