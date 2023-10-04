import re


def is_valid_email(email):  # type: (str) -> bool
    """
    Check if a string corresponds to a valid email address.

    Args:
        email (str): The input string to be checked.

    Returns:
        bool: True if email is a valid email address, False otherwise.
    """
    pattern = re.compile(
        r"^(?![.])[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    )
    return isinstance(email, str) and re.match(pattern, email) is not None
