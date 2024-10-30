#!/usr/bin/env python3
"""
This function safely retrieves a value from a dictionary
"""

from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default:
                     Union[T, None] = None) -> Union[Any, T]:
    """Documented function"""
    if key in dct:
        return dct[key]
    else:
        return default
