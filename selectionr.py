def recursive_selection_sort(arr, start=0):
    if start >= len(arr) - 1:
        return
    min_index = start
    for i in range(start + 1, len(arr)):
        if arr[i] < arr[min_index]:
            min_index = i
    arr[start], arr[min_index] = arr[min_index], arr[start]
    recursive_selection_sort(arr, start + 1)

arr = [64, 25, 12, 22, 11]
recursive_selection_sort(arr)
print(arr)