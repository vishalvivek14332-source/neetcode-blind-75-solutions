class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            element = target - nums[i]
            if element in seen:
                return [seen[element],i]
            seen[nums[i]] = i