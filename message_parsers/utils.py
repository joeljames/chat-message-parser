def force_str(value, encoding='utf-8'):
    """
    Forces the value to a str instance, decoding if necessary.
    """
    if isinstance(value, bytes):
        return str(value, encoding)
    else:
        return value
