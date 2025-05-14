import time
import random
import pandas as pd

# Iterative Insertion Sort
def insertion_sort_iterative(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1
            swaps += 1
        arr[j + 1] = key
        comparisons += 1
    return comparisons, swaps

# Recursive Insertion Sort
def insertion_sort_recursive(arr, n=None, comparisons=0, swaps=0):
    if n is None:
        n = len(arr)
    if n <= 1:
        return comparisons, swaps
    comparisons, swaps = insertion_sort_recursive(arr, n - 1, comparisons, swaps)
    key = arr[n - 1]
    j = n - 2
    while j >= 0 and arr[j] > key:
        comparisons += 1
        arr[j + 1] = arr[j]
        j -= 1
        swaps += 1
    arr[j + 1] = key
    comparisons += 1
    return comparisons, swaps

def perform_test(arr, method="iterative"):
    if method == "iterative":
        start_time = time.time()
        arr_copy = arr.copy()
        comparisons, swaps = insertion_sort_iterative(arr_copy)
        end_time = time.time()
    else:
        start_time = time.time()
        arr_copy = arr.copy()
        comparisons, swaps = insertion_sort_recursive(arr_copy)
        end_time = time.time()

    execution_time = end_time - start_time
    return execution_time, comparisons, swaps, arr_copy

test_cases = {
    "Already Sorted": [i for i in range(1, 26)],
    "Reverse Sorted": [i for i in range(25, 0, -1)],
    "Random Order": [16, 1, 4, 2, 12, 9, 10, 3, 5, 24, 14, 20, 6, 23, 7, 25, 19, 18, 8, 22, 11, 17, 13, 15, 21],
    "Nearly Sorted": [24, 25, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 1, 2],
    "Single Element at the End": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 1],
}

results = []
for name, arr in test_cases.items():
    print(f"Initial Array ({name}): {arr}")
    iterative_time, iterative_comparisons, iterative_swaps, iterative_sorted = perform_test(arr, "iterative")
    recursive_time, recursive_comparisons, recursive_swaps, recursive_sorted = perform_test(arr, "recursive")
    results.append({
        "Test Case": name,
        "Iterative Time": iterative_time,
        "Iterative Comparisons": iterative_comparisons,
        "Iterative Swaps": iterative_swaps,
        "Recursive Time": recursive_time,
        "Recursive Comparisons": recursive_comparisons,
        "Recursive Swaps": recursive_swaps
    })
    print(f"Sorted Array (Iterative): {iterative_sorted}")
    print(f"Sorted Array (Recursive): {recursive_sorted}\n")

df = pd.DataFrame(results)
print(df)