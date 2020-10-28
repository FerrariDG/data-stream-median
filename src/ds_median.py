"""Module to compute the median value on a data stream of numbers."""
from heapq import (
    heappop,
    heappush
)


class InvalidDataType(Exception):
    """Error caused by data type not float compatible."""

    pass


class NoDataOnStream(Exception):
    """Empty data structures to compute the median value."""

    pass


class MaxHeapObj:
    """Mask the behaviour of the max heap element."""

    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        """Change the behaviour of the 'lower than' operator.

        This will convert the min heap to a max heap.
        """
        return self.value > other.value

    def __eq__(self, other):
        """Define the equal operator."""
        return self.value == other.value

    def __str__(self):
        """Return a string version of the value."""
        return str(self.value)


class MinHeap:
    """Wrapper around the default min heap from heapq."""

    def __init__(self):
        self.heap = []

    def clear(self):
        """Delete all values from the heap."""
        self.heap.clear()

    def push(self, value):
        """Insert value into the heap."""
        heappush(self.heap, value)

    def pop(self):
        """Remove the lowest value from the heap."""
        return heappop(self.heap)

    def __getitem__(self, i):
        """Get the i-th value from the heap."""
        return self.heap[i]

    def __len__(self):
        """Return the number of values in the heap."""
        return len(self.heap)

    def __str__(self):
        """Return a string version of the heap."""
        return str(self.heap)


class MaxHeap(MinHeap):
    """Implement a max heap based on the default min heap.

    Encapsulate the number as a MaxHeapObj inverting the min heap to a max heap.
    """

    def push(self, value):
        """Insert value into the heap."""
        heappush(self.heap, MaxHeapObj(value))

    def pop(self):
        """Remove the highest value from the heap."""
        return heappop(self.heap).value

    def __getitem__(self, i):
        """Get the i-th value from the heap."""
        return self.heap[i].value

    def __str__(self):
        """Return a string version of the heap."""
        return str([x.value for x in self.heap])


class DataStreamMedian:
    """Compute the median value for a data stream.

    Notes
    -----
    - Can be used with int and float types.
    - Keeps two heap objects with the stream splited around the median value.

    Attributes
    ----------
    lowers: MaxHeap
        Stores the numbers lower than the median value.
        The number with the maximum value will be on the first position.

    highers: MinHeap
        Stores the numbers higher than the median value.
        The number with the minimum value will be on the first position.
    """

    def __init__(self):
        self.lowers = MaxHeap()
        self.highers = MinHeap()

    def clear(self):
        """Delete all values stored on the heaps."""
        self.lowers.clear()
        self.highers.clear()

    def add(self, number: float):
        """Add the number to the respective heap.

        Notes
        -----
        - The highers heap will have the first number.
        - The highers heap always will have the extra number when the data stream length is odd.
        - The code keeps both heaps balanced around the median value.

        Parameters
        ----------
        number : float
            Value to be added to the heap object.

        Raises
        ------
        InvalidDataType
            Occurs when the parameter 'number' has the wrong type.
        """
        try:
            float(number)
        except (TypeError, ValueError):
            raise InvalidDataType("The number parameter must be a FLOAT type compatible.")

        self.highers.push(float(number))
        self.lowers.push(self.highers.pop())

        if len(self.highers) < len(self.lowers):
            self.highers.push(self.lowers.pop())

    def compute(self) -> float:
        """Calulate the median value of the data stream.

        Notes
        -----
        - If the highers length is greater than the median value is the highers first position.
        - Else, is the mean between the first position of both heaps.

        Returns
        -------
        float
            The median value.

        Raises
        ------
        NoDataOnStream
            Occurs when the heaps objetcs are empty.
        """
        if len(self.lowers) == 0 and len(self.highers) == 0:
            raise NoDataOnStream("There is no data to compute median value.")

        return self.highers[0] if len(self.highers) > len(self.lowers) else (self.lowers[0] + self.highers[0]) / 2


if __name__ == "__main__":

    median = DataStreamMedian()

    try:
        median.compute()
    except NoDataOnStream:
        print("Add data to compute stream median")

    print("Simulating stream")

    stream = [6, 10, 2, 6, 5, 0, 6, 3, 1, 0, 0, 10]

    for idx, value in enumerate(stream):
        median.add(value)
        print(f"Stream: {stream[0:idx + 1]}")
        print(f"Lowers Heap: {median.lowers}")
        print(f"Highers Heap: {median.highers}")
        print(f"Median: {median.compute()}\n")
