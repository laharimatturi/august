class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mn=min(nums)
        mx=max(nums)
        while mn!=0:
            mn,mx=mx%mn,mn
        return mx
        
