# tests/test_[cli.py](https://cli.py)

from fibonacci_tdd_kata.cli import build_parser

def test_parser_accepts_single_number():
    args = build_parser().parse_args(["15"])
    assert args.n == 15

def test_parser_accepts_range():
    args = build_parser().parse_args(["--start", "1", "--end", "5"])
    assert args.start == 1
    assert args.end == 5
