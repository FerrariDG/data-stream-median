# Compute Median on Data Stream

This repo contains a class able to compute and hold the median value througth a data stream input.

**ds_median** - Module to compute the median value on a data stream of numbers.

## Classes
* Exceptions
    * [InvalidDataType](#InvalidDataType)
    * [NoDataOnStream](#NoDataOnStream)
* [MaxHeapObj](#MaxHeapObj)
* [MinHeap](#MinHeap)
* [MaxHeap](#MaxHeap)
* [DataStreamMedian](#DataStreamMedian)

---

### InvalidDataType

```text
Error caused by data type not float compatible.
```

### NoDataOnStream

```
Empty data structures to compute the median value.
```

### MaxHeapObj

```
Mask the behaviour of the max heap element.

Methods defined here:

__eq__(self, other)
    Define the equal operator.

__lt__(self, other)
    Change the behaviour of the 'lower than' operator.

    This will convert the min heap to a max heap.

__str__(self)
    Return a string version of the value.

```

### MinHeap

```
Wrapper around the default min heap from heapq.

Methods defined here:

__getitem__(self, i)
    Get the i-th value from the heap.

__len__(self)
    Return the number of values in the heap.

__str__(self)
    Return a string version of the heap.

clear(self)
    Delete all values from the heap.

pop(self)
    Remove the lowest value from the heap.

push(self, value)
    Insert value into the heap.

```

### MaxHeap

```
Implement a max heap based on the default min heap.

Encapsulate the number as a MaxHeapObj inverting the min heap to a max heap.

Methods defined here:

__getitem__(self, i)
    Get the i-th value from the heap.

__str__(self)
    Return a string version of the heap.

pop(self)
    Remove the highest value from the heap.

push(self, value)
    Insert value into the heap.

```

### DataStreamMedian

```text
Compute the median value for a data stream.

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

Methods defined here:

add(self, number: float)
    Add the number to the respective heap.

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

clear(self)
    Delete all values stored on the heaps.

compute(self) -> float
    Calulate the median value of the data stream.

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

```
