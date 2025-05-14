import time
import random
import pandas as pd

# Iterative Selection Sort
def selection_sort_iterative(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
    return comparisons, swaps

# Recursive Selection Sort
def selection_sort_recursive(arr, start=0, comparisons=0, swaps=0):
    n = len(arr)
    if start == n - 1:
        return comparisons, swaps
    min_idx = start
    for i in range(start + 1, n):
        comparisons += 1
        if arr[i] < arr[min_idx]:
            min_idx = i
    if min_idx != start:
        arr[start], arr[min_idx] = arr[min_idx], arr[start]
        swaps += 1
    return selection_sort_recursive(arr, start + 1, comparisons, swaps)

def perform_test(arr, method="iterative"):
    if method == "iterative":
        start_time = time.time()
        arr_copy = arr.copy()
        comparisons, swaps = selection_sort_iterative(arr_copy)
        end_time = time.time()
    else:
        start_time = time.time()
        arr_copy = arr.copy()
        comparisons, swaps = selection_sort_recursive(arr_copy)
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