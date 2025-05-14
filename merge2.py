import time 

def merge(left, right):
    merged = []
    i = j = 0
    comparisons = 0
    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged, comparisons

def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    
    mid = len(arr) // 2
    left, left_comparisons = merge_sort(arr[:mid])
    right, right_comparisons = merge_sort(arr[mid:])
    
    merged, merge_comparisons = merge(left, right)
    
    total_comparisons = left_comparisons + right_comparisons + merge_comparisons
    
    return merged, total_comparisons

def perform_test(arr):
    start_time = time.time()
    sorted_arr, comparisons = merge_sort(arr)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time, comparisons, sorted_arr

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
    execution_time, comparisons, sorted_arr = perform_test(arr)
    results.append({
        "Test Case": name,
        "Execution Time": execution_time,
        "Comparisons": comparisons
    })
    print(f"Sorted Array: {sorted_arr}\n")

import pandas as pd
df = pd.DataFrame(results)
print(df)