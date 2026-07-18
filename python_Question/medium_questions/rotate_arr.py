def rotate_array(arr, k):
    if not arr:
        return arr
    k = k % len(arr)
    return arr[-k:] + arr[:-k] if k else arr[:]

# Test
print(rotate_array([1, 2, 3, 4, 5], 2))
print(rotate_array([1, 2, 3], 1))
print(rotate_array([1, 2, 3], 3))