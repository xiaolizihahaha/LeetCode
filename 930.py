class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        res = self.helper(nums,goal) - self.helper(nums,goal-1)
        print(res)
        return res

    def helper(self,nums,limit):
        left = 0
        right = 0
        sum = 0
        res = 0

        while right < len(nums):
            sum += nums[right]
            right += 1
            while left < right and sum > limit:
                sum -= nums[left]
                left += 1

            res += right - left + 1

        return res





if __name__ == '__main__':
    nums = [0, 0, 0, 0, 0]
    goal = 0
    # nums = [1, 0, 1, 0, 1]
    # goal = 2

    # nums = [1,0,1,0,1,0,0,1,0,0,1]
    # goal = 3


    solution = Solution()
    solution.numSubarraysWithSum(nums,goal)