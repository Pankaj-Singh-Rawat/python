# quick sort -> quick sort + partition
# time complexity = O(n log n)

def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[j], array[i] = array[i], array[j]

    array[i+1], array[high] = array[high], array[i+1]
    return i + 1


def quick_sort(array, low, high):
    if low < high:
        pivot_index = partition(array, low, high)
        quick_sort(array, low, pivot_index - 1)
        quick_sort(array, pivot_index + 1, high)
    return array

arr = [23,1,45,65,2,4,456]
print(quick_sort(arr, 0, len(arr) - 1))
