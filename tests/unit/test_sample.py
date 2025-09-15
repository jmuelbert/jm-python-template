# SPDX-License-Identifier: EUPL-1.2
# SPDX-FileCopyrightText: 2023-present Jürgen Mülbert <juergen.muelbert@outlook.de>
#
# file: test_example.py


def add(a: int, b: int) -> int:
    """Simple function we want to test."""
    return a + b


def test_add_positive_numbers():
    """Test that add() works with positive numbers."""
    expected_result: int = 5
    assert add(2, 3) == expected_result


def test_add_negative_numbers():
    """Test that add() works with negative numbers."""
    expected_result: int = -2
    assert add(-1, -1) == expected_result


def test_add_mixed_numbers() -> None:
    """Test that add() works with a mix of positive and negative."""
    assert add(-2, 3) == 1
