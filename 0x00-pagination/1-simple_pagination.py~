#!/usr/bin/env python3
"""Pagination"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Function retrieves the index rnage from a given page and
    its page size"""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
