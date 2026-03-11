def search(iterable, search_item):
    """
    Searches for first occurance of given search item over sorted iterable object using binary search algorithm. 
    
    Args:
        Sorted iterable object (list)
        Element to be searched
    Returns:
        Index of first occurance of search element, 0 for empty iterable; otherwise -1
            
    Raises:
        TypeError: If the iterable object is not iterable
        TypeError: IF the interable object does not support indexing
        TypeError: If the data type of the first item is not the same as the search item

    Only allows for binary search of single string element in larger string
    """
    # Check for iterability and indexable sequence object
    if not hasattr(iterable, "__getitem__") or not hasattr(iterable, "__len__"):
        raise TypeError(f"'{type(iterable).__name__}' object does not support indexing.")
    
    # Check for comparability and emptiness
    if len(iterable) == 0:
        return -1
    
    try:
        first_item = iterable[0]
        first_item < search_item
    except TypeError:
        raise TypeError (f"'<' not supported between instances of '{type(first_item).__name__}' and '{type(search_item).__name__}'")    
    
    return _binary_search(iterable, search_item, 0, len(iterable) - 1)


def _binary_search(iterable, search_item, left, right):
    """
    Internal binary search function for sorted iterables using recursive method.
    
    Args:
        Sorted iterable object (list)
        Element to be searched
        Left index boundary for search range
        Right index boundary for search range
    
    Returns:
        Index of first occurance of search element, or -1 if not found.
    """
    # End of rescursive search without finding the element
    if left > right:
        return -1
    # Pointer adds the mid-point of distance between ends to the lower bound to avoid number overflow
    pointer = left + ((right - left) // 2)
    if iterable[pointer] == search_item:
        if pointer > 0 and iterable[pointer - 1] == search_item:
            return _binary_search(iterable, search_item, left, pointer - 1)
        return pointer
    elif iterable[pointer] < search_item:
        return _binary_search(iterable, search_item, pointer + 1, right)
    else:
        return _iterative_binary_search(iterable, search_item)#, left, pointer - 1)

def _iterative_binary_search(iterable, search_item):
    """
    Internal binary search function for sorted iterables using iterative method.
    
    Args:
        Sorted iterable object (list)
        Element to be searched
    
    Returns:
        Index of first occurance of search element, or -1 if not found.
    """
    left = 0
    right = len(iterable) - 1
    # result = -1
    while left <= right:
        pointer = left + ((right - left) // 2)
        if iterable[pointer] == search_item:
            # result = pointer 
            ## #Always do they check and move the right pointer closer in case of a long sequence of same item
            if pointer > 0 and iterable[pointer - 1] == search_item: 
                right  = pointer - 1
            else:
                return pointer         
        elif iterable[pointer] < search_item:
            left = pointer + 1
        else:
            right = pointer - 1  
    
    return -1

# result = search([], 3)
result = search("aaabbcc", "d")
# result = search({1,2,3}, 2)
# result = search([True, False], 1)
# result = search(["a","b","c"], 3)
# result = search([1,2,3], "hello")
# result = search([1,2,3], 2.0)
# result = search(2, 2)
print(result)

    