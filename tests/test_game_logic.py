import sys
from pathlib import Path

# Ensure repo root is on sys.path so tests can import top-level modules
sys.path.append(str(Path(__file__).resolve().parents[1]))

from logic_utils import check_guess


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
