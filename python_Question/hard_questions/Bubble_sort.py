def bubble_sort(arr):
    arr = arr[:]
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Test
print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
print(bubble_sort([5, 1, 4, 2, 8]))
print(bubble_sort([1]))