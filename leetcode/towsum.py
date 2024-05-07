class Solution:
    def twosum(self, nums: List[int], target: int) -> List[int]:
        _nums = {}
        length = len(nums)
        for i in range(length):
            val = target - nums[i]
            if val in _nums:
                return [i, _nums[val]]
            _nums[nums[i]] = i
