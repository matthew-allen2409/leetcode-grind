# Assuming a majority element actually exists
def majorityElement(nums):
    candidate = -1
    count = 0

    majority = len(nums) / 2 + 1

    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    return candidate
