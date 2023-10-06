import re

# FORMATTING
############


def format_processo_juridico(legal_process_id):  # type: (str) -> (str)
    """
    Format an adequately formatted numbers-only Legal Process ID number,
    Returns a Legal Process ID number formatted with standard visual aid symbols.
    Returns None if Legal Process ID number is invalid.
    """
    if legal_process_id.isdigit() and len(legal_process_id) == 20:
        capture_fields = r"(\d{7})(\d{2})(\d{4})(\d)(\d{2})(\d{4})"
        include_chars = r"\1-\2.\3.\4.\5.\6"
        return re.sub(capture_fields, include_chars, legal_process_id)
    return None


def remove_symbols(processo_juridico: str):  # type: (str) -> str
    """Removes common symbols from a legal process number string.
    The standard symbols removed are "." and "-"

    Args:
                    process_juridico[str]: A legal process number string
    Returns:
                    [str]: A legal process number string without symbols
    """
    return processo_juridico.replace(".", "").replace("-", "")
