def binary_search(arr, x):
    return binary_search_recursive(arr, 0, len(arr) - 1, x)

def binary_search_recursive(arr, low, high, x):
    if low > high:
        return -1

    mid = (low + high) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] < x:
        return binary_search_recursive(arr, mid + 1, high, x)
    else:
        return binary_search_recursive(arr, low, mid - 1, x)