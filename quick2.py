import random
import time
import pandas as pd

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    comparisons = 0
    swaps = 0
    for j in range(low, high):
        comparisons += 1
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)
            swaps += 1
    swap(arr, i + 1, high)
    swaps += 1
    return i + 1, comparisons, swaps

def randomized_partition(arr, low, high):
    rand_index = random.randint(low, high)
    swap(arr, rand_index, high)
    return partition(arr, low, high)

def quick_sort(arr, low, high):
    comparisons = 0
    swaps = 0
    if low < high:
        pi, comp, swap = randomized_partition(arr, low, high)
        comparisons += comp
        swaps += swap
        
        left_comparisons, left_swaps = quick_sort(arr, low, pi - 1)
        right_comparisons, right_swaps = quick_sort(arr, pi + 1, high)
        
        comparisons += left_comparisons + right_comparisons
        swaps += left_swaps + right_swaps

    return comparisons, swaps

def perform_test(arr):
    start_time = time.time()
    comparisons, swaps = quick_sort(arr, 0, len(arr) - 1)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time, comparisons, swaps, arr

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
    execution_time, comparisons, swaps, sorted_arr = perform_test(arr.copy())
    results.append({
        "Test Case": name,
        "Execution Time": execution_time,
        "Comparisons": comparisons,
        "Swaps": swaps
    })
    print(f"Sorted Array: {sorted_arr}\n")

df = pd.DataFrame(results)
print(df)