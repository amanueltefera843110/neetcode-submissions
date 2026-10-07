class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter=Counter(nums)
        l=[]
        for i,v in counter.most_common(k):
            l.append(i)
        return l


       

        