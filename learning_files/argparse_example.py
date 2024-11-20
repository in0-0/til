import argparse

parser = argparse.ArgumentParser(
    prog="ProgramName",
    description="What the program does",
    epilog="Text at the bottom of help",
)


parser.add_argument("-f", "--foo")
parser.add_argument("bar")
parser.add_argument("--act", action="store_true")
parser.add_argument("--def", default=999)
parser.add_argument("--cho", choices=[1, 2, 3])
parser.add_argument("--ty", type=ascii)
parser.add_argument("--reqf", required=False)
parser.add_argument("--hel", help="help text")
parser.print_help()

parser.parse_args(["BAR", "--reqf", "123"])
argparse.Namespace(bar="BAR", foo=None)
arg = parser.parse_args(["BAR", "--foo", "FOO"])
print(arg)
argparse.Namespace(bar="BAR", foo="FOO")
arg = parser.parse_args(["--foo", "FOO"])
print(arg)
# usage: PROG [-h] [-f FOO] bar
# PROG: error: the following arguments are required: bar
