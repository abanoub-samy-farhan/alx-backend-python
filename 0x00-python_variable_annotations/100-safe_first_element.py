#!/usr/bin/env python3
"""
Module with utility functions for working with lists.
"""


from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None
