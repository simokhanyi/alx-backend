#!/usr/bin/env python3
"""
Main file
"""


def index_range(page, page_size):
    """
    Return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for the given
    pagination parameters.

    Arguments:
    page -- the current page number (1-indexed)
    page_size -- the number of items per page
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


# Test cases
if __name__ == "__main__":
    res = index_range(1, 7)
    print(type(res))  # Expected output: <class 'tuple'>
    print(res)        # Expected output: (0, 7)

    res = index_range(page=3, page_size=15)
    print(type(res))  # Expected output: <class 'tuple'>
    print(res)        # Expected output: (30, 45)
