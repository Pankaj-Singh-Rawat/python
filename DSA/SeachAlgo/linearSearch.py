def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    
    return -1

nums = [123,34,4,5,576,6,8,89]
print(linearSearch(nums, 89))

# time complexity -> O(n)
# Best case -> O(1)
# Worst Case -> O(n)
