'''
Given an array of integers nums, return the number of good pairs.
A pair (i, j) is called good if nums[i] == nums[j] and i < j
Input: nums = [1,2,3,1,1,3]
Output: 4
'''

class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer=0
        for i in range(len(nums)):
            count=0
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    count=count+1
            answer=answer+count
        return answer

    print(numIdenticalPairs("self",[1,2,3,1,1,3]))