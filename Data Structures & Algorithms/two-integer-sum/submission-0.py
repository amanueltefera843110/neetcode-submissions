class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}

        for i in range(len(nums)):
            tem=target-nums[i]
            if tem in seen:
                return[seen[tem],i]
            seen[nums[i]] = i
        return []
        
        
        