"""
This does a thing maybe?
"""
from riskan.something.stuff import blah


def add_arguments(parser):
    parser.add_argument(
        "-e", "--extra", help="Something else to add", type=str, default=""
    )
    return parser


def execute(args):
    print(f"{blah()} {args.extra}")
