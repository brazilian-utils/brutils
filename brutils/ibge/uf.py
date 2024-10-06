def convert_uf_to_text(uf):  # type: (str) -> str | None
    """
    Converts a given Brazilian state code (UF) to its full state name.

    This function takes a 2-letter UF code and returns the corresponding full state name.
    It handles all Brazilian states and the Federal District.

    Args:
        uf (str): The 2-letter UF code to be converted.

    Returns:
        str or None: The full name of the state corresponding to the UF code,
            or None if the UF code is invalid.

    Example:
        >>> convert_uf_to_text('SP')
        "São Paulo"
        >>> convert_uf_to_text('RJ')
        "Rio de Janeiro"
        >>> convert_uf_to_text('XX')
        None
    """

    from brutils.data.enums.uf import UF

    try:
        return UF[uf.upper()].value
    except KeyError:
        return None
