"""Tests the {{ cookiecutter.package_name }} project's CLI."""

from {{ cookiecutter.package_name }} import main


def test_main() -> None:
    """Tests main() function."""
    assert main([""]) == 0
