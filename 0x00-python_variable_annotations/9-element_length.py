#!/usr/bin/env python3
"""Type-annotated function element_length that takes a list as argument and
returns the values with the appropriate types
"""


from typing import Sequence, Union, List, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Type-annotated function element_length that takes a list as argument and"""
    return [(i, len(i)) for i in lst]
