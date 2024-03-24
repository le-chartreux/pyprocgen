import unittest.mock
from unittest.mock import Mock

from pyprocgen.__main__ import cli, version


@unittest.mock.patch("pyprocgen.__main__.print")
def test_cli(mock_print: Mock) -> None:
    cli()
    mock_print.assert_called_once_with("hello world!")


@unittest.mock.patch("pyprocgen.__main__.print")
def test_version(mock_print: Mock) -> None:
    version()
    mock_print.assert_called_once_with("2.0.0")
