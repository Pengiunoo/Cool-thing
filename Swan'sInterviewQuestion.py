
def singleNumber(nums: [int]) -> int:
    pie = 0
    for num in nums:
        pie ^= num

    return pie
singleNumber(nums = [1 ,1, 2, 2, 3])
