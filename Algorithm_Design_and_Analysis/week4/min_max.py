def find_min_max(arr, low, high):
    # Base case: n = 1
    if low == high:
        return arr[low], arr[low]

    # Base case: n = 2
    elif low + 1 == high:
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    # Divide the array into two parts
    else:
        mid = (low + high) // 2
        min1, max1 = find_min_max(arr, low, mid)
        min2, max2 = find_min_max(arr, mid + 1, high)

        # Merge the results
        return min(min1, min2), max(max1, max2)