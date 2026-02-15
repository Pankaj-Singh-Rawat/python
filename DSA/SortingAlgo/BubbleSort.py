def bubbleSort(nums):
    n = len(nums)
    for i in range(n-1):
        for j in range (n - i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    return nums
nums = [64, 34, 25, 12, 22, 11, 90, 5]
print(bubbleSort(nums))

# time complexity -> O(n^2)