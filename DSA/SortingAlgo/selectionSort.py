nums = [ 7, 12, 9, 11, 3, 2]

def selectionSort(nums):
    n = len(nums)
    for i in range (n - 1):
        min = i
        for j in range(i+1, n):
            if nums[j] < nums[min]:
                min = j
        minValue = nums.pop(min)
        nums.insert(i , minValue)
    return nums

print(selectionSort(nums))
