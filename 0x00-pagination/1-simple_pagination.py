#!/usr/bin/env python3
"""
Main cvs file
"""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a page from the dataset.

        Arguments:
        page -- the current page number (1-indexed)
        page_size -- the number of items per page

        Returns:
        A list of lists representing the data on the specified page.
        """
        assert isinstance(page, int), "page must be a positive integer"
        assert page > 0, "page must be a positive integer"
        assert isinstance(page_size, int), "page_size must be positive integer"
        assert page_size > 0, "page_size must be a positive integer"

        start_index, end_index = index_range(page, page_size)
        data = self.dataset()

        if start_index >= len(data):
            return []

        return data[start_index:end_index]


# Test cases
if __name__ == "__main__":
    server = Server()

    try:
        should_err = server.get_page(-10, 2)
    except AssertionError:
        print("AssertionError raised with negative values")

    try:
        should_err = server.get_page(0, 0)
    except AssertionError:
        print("AssertionError raised with 0")

    try:
        should_err = server.get_page(2, 'Bob')
    except AssertionError:
        print("AssertionError raised when page and/or page_size are not ints")

    print(server.get_page(1, 3))  # Expected output: First 3 records
    print(server.get_page(3, 2))  # Expected output: 5th and 6th records
    print(server.get_page(3000, 100))  # Expected output: []
