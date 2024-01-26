#!/usr/bin/env python3

""" defines function index_range """

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates the start and end index for a specific
    page and page size in a list.
    """
    start_index = (page - 1) * page_size

    end_index = start_index + page_size

    return (start_index, end_index)
