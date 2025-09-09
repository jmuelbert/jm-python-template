"""Example build process functions for testing coverage and pytest."""

from __future__ import annotations


def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


def divide(a: float, b: float) -> float:
    """
    Divide `a` by `b`.

    Raises:
        ZeroDivisionError: If `b` is zero.
    """
    msg = "Division by zero is not allowed."
    if b == 0:
        raise ZeroDivisionError(msg)
    return a / b


def build_pipeline(steps: list[str]) -> str:
    """
    Simulate a build pipeline.

    Args:
        steps: A list of build step names.

    Returns:
        str: A string summary of the pipeline execution.
    """
    if not steps:
        return "No steps to run."

    executed = [f"Executed {step}" for step in steps]
    return " | ".join(executed)


def conditional_process(*, flag: bool) -> str:
    """Run a conditional process depending on the flag."""
    if flag:
        return "Process executed."
    return "Process skipped."
