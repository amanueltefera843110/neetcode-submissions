class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        count=Counter(nums)
        m=max(count.values())
        return True if m>1 else False