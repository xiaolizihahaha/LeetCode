class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        jisuan = [0] * (len(nums) + 1)
        jisuan[0] = 0


        for i in range(len(nums)):
            if nums[i] == 1:
                jisuan[i+1] = jisuan[i] + 1
            else:
                jisuan[i+1] = 0

        print(max(jisuan))
        return max(jisuan)


if __name__ == '__main__':
    nums = [1, 1, 0, 1, 1, 1]
    nums = [1, 0, 1, 1, 0, 1]
    solution = Solution()
    solution.findMaxConsecutiveOnes(nums)
