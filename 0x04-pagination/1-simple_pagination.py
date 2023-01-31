#!/usr/bin/env python3
"""1-simple_pagination module"""
import csv
import math
from typing import List


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
        """gets the requested page items"""
        assert type(page) is not int or type(page_size) is not int
        assert page <= 0 or page_size <= 0
        self.__dataset: List[List] = self.dataset()
        indxRange: tuple = index_range(page, page_size)
        range1: int = indxRange[0]
        range2: int = indxRange[1]
        return self.__dataset[range1:range2]


def index_range(page: int, page_size: int) -> tuple:
    """return a tuple of size two containing a start index and an
        end index corresponding to the range of indexes to return in a
    list for those particular pagination parameters."""
    return (((page*page_size)-page_size, (page*page_size)))
