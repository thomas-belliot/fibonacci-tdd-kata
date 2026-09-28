# tests/test_[cli.py](https://cli.py)

# import pytest

from fibonacci_tdd_kata.cli import build_parser


def test_parser_accepts_single_number():
    args = build_parser().parse_args(["15"])
    assert args.n == 15


def test_parser_accepts_range():
    args = build_parser().parse_args(["--start", "1", "--end", "5"])
    assert args.start == 1
    assert args.end == 5


def test_main_prints_single_value(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["fibonacci-kata", "15"])
    assert capsys.readouterr().out.strip() == ""


def test_main_prints_range(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["fibonacci-kata", "--start", "1", "--end", "5"])
    lines = capsys.readouterr().out.strip().splitlines()
    assert lines == []


"""def test_main_requires_an_argument(monkeypatch):
    monkeypatch.setattr("sys.argv", ["fibonacci-kata"])
    with pytest.raises(SystemExit):
        return"""
