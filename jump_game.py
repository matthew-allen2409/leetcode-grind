def canJump(nums):
    curr = 0

    while curr < len(nums):
        jump_potential = curr + nums[curr]
        if jump_potential >= len(nums) - 1:
            return True
        if jump_potential == curr:
            return False

        index = curr
        while index < jump_potential:
            index += 1
            print("index:", index)
            if nums[index] >= nums[curr]:
                curr = index

    return True

nums = [3, 2, 1, 0, 4]

print(canJump(nums))
