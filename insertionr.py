def recursive_insertion_sort(arr, n=None):
    if n is None:
        n = len(arr)
    if n <= 1:
        return
    recursive_insertion_sort(arr, n - 1)
    last = arr[n - 1]
    j = n - 2
    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = last

arr = [64, 25, 12, 22, 11]
recursive_insertion_sort(arr)
print(arr)