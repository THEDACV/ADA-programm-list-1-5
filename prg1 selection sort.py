def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i  # Assume the current index is the minimum
        for j in range(i + 1, len(arr)):  # Iterate through the unsorted part
            if arr[j] < arr[min_idx]:  # Find the smallest element
                min_idx = j  # Update min_idx if a smaller element is found
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap the found minimum with the first unsorted element

# Example usage
data = [64, 34, 25, 12, 22]
selection_sort(data)
print("Sorted array:", data)