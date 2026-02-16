def insertionSort(nums):
    for i in range (1, len(nums)):
        index = i
        value = nums.pop(i)
        for j in range(i - 1, -1, -1):
            if nums[j] > value:
                index = j
            
        nums.insert(index, value)

    return nums

nums = [64, 34, 25, 12, 22, 11, 90, 5]
print(insertionSort(nums))

