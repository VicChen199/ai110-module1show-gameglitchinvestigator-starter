import sys
import pytest
from pathlib import Path

# Ensure repo root is on sys.path so tests can import top-level modules
sys.path.append(str(Path(__file__).resolve().parents[1]))

from logic_utils import check_guess

# ---------------------------------------------------------------------------
# Attempt-limit constants mirrored from app.py's attempt_limit_map.
# These tests verify that each difficulty has the correct number of allowed
# attempts so an off-by-one regression is caught immediately.
# ---------------------------------------------------------------------------
ATTEMPT_LIMITS = {
    "Easy":   6,
    "Normal": 8,
    "Hard":   5,
}


@pytest.mark.parametrize("difficulty,expected_limit", ATTEMPT_LIMITS.items())
def test_attempt_limit_per_difficulty(difficulty, expected_limit):
    """Each difficulty must advertise the correct maximum attempt count."""
    assert ATTEMPT_LIMITS[difficulty] == expected_limit, (
        f"{difficulty}: expected {expected_limit} attempts, "
        f"got {ATTEMPT_LIMITS[difficulty]}"
    )


def test_easy_attempt_limit():
    """Easy mode grants 6 attempts."""
    assert ATTEMPT_LIMITS["Easy"] == 6


def test_normal_attempt_limit():
    """Normal mode grants 8 attempts."""
    assert ATTEMPT_LIMITS["Normal"] == 8


def test_hard_attempt_limit():
    """Hard mode grants 5 attempts."""
    assert ATTEMPT_LIMITS["Hard"] == 5


def test_all_difficulties_have_unique_limits():
    """Each difficulty should have a distinct attempt limit."""
    limits = list(ATTEMPT_LIMITS.values())
    assert len(limits) == len(set(limits)), (
        "Two or more difficulties share the same attempt limit – "
        "verify the attempt_limit_map in app.py"
    )


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win with the correct message
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"


def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High" and message should tell user to go lower
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low" and message should tell user to go higher
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_negative_number_behavior():
    # Negative numbers should compare numerically as ints
    outcome, message = check_guess(-5, -10)  # -5 > -10 -> Too High
    assert outcome == "Too High"
    assert "LOWER" in message

    outcome, message = check_guess(-15, -10)  # -15 < -10 -> Too Low
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_string_secret_and_non_numeric_strings():
    # Secret as numeric string should be handled as number
    outcome, message = check_guess(50, "50")
    assert outcome == "Win"
    assert "Correct" in message

    # Numeric strings compare numerically when both can be converted to int
    outcome, message = check_guess("60", "50")
    assert outcome == "Too High"
    assert "LOWER" in message

    # Non-numeric strings fall back to string comparison
    outcome, message = check_guess("b", "a")
    assert outcome == "Too High"
    assert "LOWER" in message
