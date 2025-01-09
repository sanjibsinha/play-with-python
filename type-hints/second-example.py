from typing import List, Dict, Tuple, Union, Optional, Callable, TypeVar, Generic

T = TypeVar('T')

class DataProcessor(Generic[T]):
    """
    A class demonstrating various type hints.
    """

    def __init__(self, data: List[T]) -> None:
        """
        Initializes the DataProcessor with a list of data.

        Args:
            data: A list of data elements.
        """
        self.data = data

    def process_data(self, 
                    callback: Callable[[T], Union[str, int]]) -> List[Union[str, int]]:
        """
        Processes the data using a callback function.

        Args:
            callback: A function that takes a data element as input 
                      and returns either a string or an integer.

        Returns:
            A list of processed data elements.
        """
        processed_data: List[Union[str, int]] = []
        for item in self.data:
            processed_data.append(callback(item))
        return processed_data

    def get_data_by_index(self, index: int) -> Optional[T]:
        """
        Gets a data element by its index.

        Args:
            index: The index of the data element.

        Returns:
            The data element at the given index, or None if the index is out of bounds.
        """
        try:
            return self.data[index]
        except IndexError:
            return None

    def group_data(self) -> Dict[T, List[T]]:
        """
        Groups the data elements by their values.

        Returns:
            A dictionary where keys are data elements and values are lists 
            of elements with the same value.
        """
        grouped_data: Dict[T, List[T]] = {}
        for item in self.data:
            if item in grouped_data:
                grouped_data[item].append(item)
            else:
                grouped_data[item] = [item]
        return grouped_data

# Example usage
data = [1, 2, 2, 3, 3, 3]
processor = DataProcessor(data)

# Using process_data with a lambda function
processed_data = processor.process_data(lambda x: x * 2 if x % 2 == 0 else str(x))
print(processed_data)  # Output: ['1', 4, 4, '3', '3', '3']

# Using get_data_by_index
element = processor.get_data_by_index(2)
print(element)  # Output: 2

# Using group_data
grouped_data = processor.group_data()
print(grouped_data)  # Output: {1: [1], 2: [2, 2], 3: [3, 3, 3]}