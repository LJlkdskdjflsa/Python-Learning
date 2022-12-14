# pyright: strict
from calculate_time.calculate_time import calculate_time


@calculate_time
def quick_sort(data_set: list[int]) -> list[int]:
    """quick sort warpper

    Args:
        data_set (list[int]):the list to be sort

    Returns:
        list[int]: the sorted list of integers
    """
    return _quick_sort(data_set)


def _quick_sort(
    data_set: list[int], left: int = 0, right: int | None = None
) -> list[int]:
    """sort list of integers by using recurrent partition

    Time complexity:
        Worst situation(reverse(need to loop n times->can use random to fix?)): O(n^2)
        Normal:O(n*log(n))

    Args:
        data_set (list[int]): the list to be sort
        left (int, optional):the left boundry of the list need to sort Defaults to 0.
        right (int | None, optional): the left boundry of the list need to sort. Defaults to None(to the last element)

    Returns:
        list[int]: the sorted list of integers
    """
    if right is None:
        right = len(data_set) - 1
    if right > left:  # at least two elements
        mid = partition(data_set, left, right)
        _quick_sort(data_set, mid + 1, right)
        _quick_sort(data_set, left, mid - 1)
    return data_set


def partition(data_set: list[int], left: int, right: int) -> int:
    """
    Returns a list that the items on the right side of the middle item is always smaller than the left side
    Time complexity:
        O(n)

    Args:
        data_set (List[int]): the data set to partition
        left (int): the left boundry index
        right (int): the right boundry index

    Returns:
        List[int]: sorted partitioned data
    """

    tmp = data_set[left]  # the middle item
    while left < right:
        while (
            left < right and data_set[right] >= tmp
        ):  # find item that is smaller than middle from right
            right -= 1
        data_set[left] = data_set[right]  # write the right value to the left
        while (
            left < right and data_set[left] <= tmp
        ):  # find item that is bigger than middle from left
            left += 1
        data_set[right] = data_set[left]  # write the left value to the right
    data_set[left] = tmp  # range the tmp value
    return left
