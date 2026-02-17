def kadaneAlge(nums: list[int]) -> int:
    currentMax = nums[0]
    endingMax = nums[0]

    for i in range(1, len(nums)):
        currentMax = max(nums[i], nums[i] + currentMax)
        endingMax = max(currentMax, endingMax)

    return endingMax

print(kadaneAlge([-2, 1, -3, 4, -1, 2, 1, -5, 4]))