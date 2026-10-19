class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        count = 0
        values = set(nums)
        for x in nums:
            if x + diff in values and x + 2*diff in values:
                count += 1
        return count