def quick_sort(arr, low, high, comparisons, swaps):
    if low < high:
        pivot_idx = partition(arr, low, high, comparisons, swaps)
        
        print(f"Pass - Pivot {arr[pivot_idx]}: {comparisons[0]} comparisons, {swaps[0]} swaps")
        
        quick_sort(arr, low, pivot_idx - 1, comparisons, swaps)
        quick_sort(arr, pivot_idx + 1, high, comparisons, swaps)
    
    return arr

def partition(arr, low, high, comparisons, swaps):
    mid = (low + high) // 2
    pivot = arr[mid]
    
    arr[mid], arr[high] = arr[high], arr[mid]
    swaps[0] += 1
    
    i = low - 1
    
    for j in range(low, high):
        comparisons[0] += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            swaps[0] += 1
            
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    swaps[0] += 1
    
    return i + 1

arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)

comparisons = [0]  
swaps = [0]

sorted_arr = quick_sort(arr, 0, len(arr)-1, comparisons, swaps)
print("\nSorted array:", sorted_arr)
print(f"\nTotal comparisons: {comparisons[0]}")
print(f"Total swaps: {swaps[0]}")
