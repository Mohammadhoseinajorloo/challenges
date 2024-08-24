from typing import List

class Solution:
	def removeElement(self, nums: List[int], val: int) -> int:
		index = 0 
		for i in range(len(nums)):
			if nums[i] != val:
				nums[index] = nums[i]
				index += 1
		return index



if __name__ == "__main__":
	nums = [0,1,2,2,3,0,4,2]
	val = 2
	result = Solution()
	k = result.removeElement(nums, val)
	print(k)
