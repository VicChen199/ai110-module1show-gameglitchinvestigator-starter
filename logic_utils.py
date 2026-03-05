def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # Try to compare numerically when possible (secret may be a string
    # occasionally in the app, so convert if it represents an int).
    try:
        g = int(guess)
    except Exception:
        g = guess

    try:
        s = int(secret)
    except Exception:
        s = secret

    # If both are integers use numeric comparison so ordering is correct.
    if isinstance(g, int) and isinstance(s, int):
        if g == s:
            return "Win", "🎉 Correct!"
        if g > s:
            # Guess is greater than secret -> it's too high; tell user to go lower.
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"

    # Fallback to string comparison for non-numeric values.
    if g == s:
        return "Win", "🎉 Correct!"
    if g > s:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
