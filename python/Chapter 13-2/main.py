def find_min(nums):
    min = float("inf")
    for i in nums:
        if min > i:
            min = i
    return min