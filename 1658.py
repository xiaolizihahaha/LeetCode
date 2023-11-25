class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """

        # 值为goal的长度最大的窗口
        goal = sum(nums) - x
        print(goal)

        r = 0
        l = 0
        sum1 = 0
        maxlength = -1

        while r < len(nums):
            sum1 += nums[r]
            r += 1

            while l < r and sum1 >= goal:
                if sum1 == goal:
                    maxlength = max(maxlength,r-l)
                sum1 -= nums[l]
                l += 1
        if sum1 == goal:
            maxlength = max(maxlength, r - l)


        if maxlength == -1:
            print(maxlength)
            return maxlength
        if maxlength != -1:
            print(len(nums) - maxlength)
            return len(nums) - maxlength





if __name__ == '__main__':
    nums = [6, 1, 1, 4, 2, 3,6,1,1,1,1,1,1]
    x = 5

    # nums = [5, 6, 7, 8, 9]
    # x = 4
    # #
    # nums = [3, 2, 20, 1, 1, 3]
    # x = 10
    solution = Solution()
    solution.minOperations(nums,x)