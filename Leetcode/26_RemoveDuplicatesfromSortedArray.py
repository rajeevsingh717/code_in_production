# 26. Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=0
        for i in range(1,len(nums)):
            if nums[l]!=nums[i]:
                l += 1 
                nums[l] = nums[i]
        return l+1
