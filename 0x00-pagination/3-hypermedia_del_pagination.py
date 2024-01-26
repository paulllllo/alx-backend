#!/usr/bin/env python3

"""
Deletion-resilient hypermedia pagination for a database of popular baby names.
"""

import csv
from typing import List, Dict


class Server:
    """
    A server class to facilitate the pagination of a
    database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initializes the Server class with the dataset and
        indexed dataset attributes.
        """
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Retrieves the cached dataset.

        Returns:
            List[List]: The cached dataset without the header.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE, 'r') as f:
                reader = csv.reader(f)
                dataset = list(reader)
            self.__dataset = dataset[1:]  # Removing the header
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Retrieves the dataset indexed by sorting position, starting at 0.

        Returns:
            Dict[int, List]: The indexed dataset.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            # Limit the dataset size for optimization
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None,\
                        page_size: int = 10) -> Dict:
        """
        Retrieves data from the indexed dataset based on
        the provided index and page size.
        Args:
            index (int): The index of the first item in the current page.
            page_size (int): The required number of records per page.

        Returns:
            Dict: A dictionary with the following key-value pairs:
                - index: The index of the first item in the current page.
                - next_index: The index of the first item in the next page.
                - page_size: The current page size.
                - data: The actual page of the dataset.
        """
        dataset = self.indexed_dataset()
        data_length = len(dataset)
        assert 0 <= index < data_length, "Invalid index value"
        response = {}
        data = []
        response['index'] = index
        for _ in range(page_size):
            while True:
                curr = dataset.get(index)
                index += 1
                if curr is not None:
                    break
            data.append(curr)

        response['data'] = data
        response['page_size'] = len(data)
        response['next_index'] = index if index < data_length else None
        return response
