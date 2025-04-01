class Solution(object):
    def containsDuplicate(self, nums):     
        length = len(nums)
        for i in range(length):
            for j in range(i+1 , length):
                if nums[i]==nums[j]:
                    return True
        return False