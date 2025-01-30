def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
        """
        ans=[]
        for i in range(len(nums)):
            for j in range (len(nums)):
                if i!=j and nums[i]+nums[j]==target:
                    ans.append(i)
                    ans.append(j)
                    return ans
        
        