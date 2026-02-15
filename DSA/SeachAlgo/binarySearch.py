def binarySearch(arr, target):
    left = 0
    right = len(arr)

    while left <= right:
        mid =left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1

nums = [1,3,5,6,8,9,24,45,67]
print(binarySearch(nums, 24))