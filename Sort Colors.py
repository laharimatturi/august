class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left = 0
        right = len(nums) - 1

       
        while left < right:
            if nums[right] == 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            else:
                right -= 1

        
        left = 0
        right = len(nums) - 1

        
        while left < right:
            if nums[left] == 2:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1
