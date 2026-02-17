# sliding window
# fixed size sliding window
arr = [1,12,-5,-6,50,3]
k = 4

def sw1(nums, k):
    current_sum = sum(nums[:k])
    max_num = current_sum

    for i in range(len(nums) - k):
        current_sum = current_sum - nums[i] + nums[i + k]
        if current_sum > max_num:
            max_num = current_sum

    return max_num/k

print(sw1(arr, k))

# use instead of nested loops