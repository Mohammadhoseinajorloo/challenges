from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp, next_ = 0 , 1
        while next_ in range(len(nums)):
            if nums[temp] == nums[next_]:
                next_+=1
            else:
                nums[temp+1] = nums[next_]
                next_+=1
                temp+=1
        return temp+1
