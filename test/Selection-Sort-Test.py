import time
import random

def selection_sort(arr):
    n = len(arr)
    comparisons = 0

    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr, comparisons


def selection_sort_recursive(arr, index=0, comparisons=0):
    if index >= len(arr) - 1:
        return arr, comparisons

    min_index = index
    for j in range(index + 1, len(arr)):
        comparisons += 1
        if arr[j] < arr[min_index]:
            min_index = j

    if min_index != index:
        arr[index], arr[min_index] = arr[min_index], arr[index]

        print(f"Swap {index+1}: {arr}")

    return selection_sort_recursive(arr, index + 1, comparisons)


test_cases = {
    "1": ("Already Sorted", list(range(1, 26))),
    "2": ("Reverse Sorted", list(range(25, 0, -1))),
    "3": ("Random Order", [16, 1, 4, 2, 12, 9, 10, 3, 5, 24, 14, 20, 6, 23, 7, 25, 19, 18, 8, 22, 11, 17, 13, 15, 21]),
    "4": ("Nearly Sorted", [24, 25, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 1, 2]),
    "5": ("Single Element at the End", [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 1]),
    "6": ("Large Input", random.sample(range(1, 101), 100)),
    "7": ("User Input", None)
}

print("Choose a test case:")
for key, value in test_cases.items():
    print(f"{key}. {value[0]}")

choice = input("Enter your choice (1-7): ")

if choice == "7":
    user_input = input("Enter numbers separated by spaces: ")
    arr = list(map(int, user_input.split()))
else:
    arr = test_cases.get(choice, ("Invalid Choice", []))[1]

if not arr:
    print("Invalid choice. Exiting...")
else:
    print("\nOriginal Array:", arr)

    print("\n--- Iterative Selection Sort ---")
    start_time = time.time()
    arr, comparisons = selection_sort(arr[:])
    end_time = time.time()
    print(f"Total comparisons: {comparisons}")
    print(f"Time taken for iterative: {end_time - start_time:.10f} seconds\n")

    print("\n--- Recursive Selection Sort ---")
    start_time = time.time()
    arr, comparisons = selection_sort_recursive(arr[:])
    end_time = time.time()
    print(f"Total comparisons: {comparisons}")
    print(f"Time taken for recursion: {end_time - start_time:.10f} seconds\n")