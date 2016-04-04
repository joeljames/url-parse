import six

import config


__all__ = [
    'force_str',
    'get_config',
]


def force_str(value, encoding='utf-8'):
    """
    Forces the value to a str instance, decoding if necessary.
    """
    if six.PY3 and isinstance(value, bytes):
        return str(value, encoding)
    else:
        return value


def get_config(key, default=None):
    """
    Get config from config module if exists,
    return default value otherwise
    """
    return getattr(config, key, default)
