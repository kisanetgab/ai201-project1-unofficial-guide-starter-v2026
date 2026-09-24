def judge(question, expects, answer, results) -> bool:
    """Return True if the answer satisfies what the question expects."""
    if answer is None:
        return False
    return str(expects).strip().lower() in str(answer).strip().lower()
