class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k >= len(nums):
            return len(nums)
        bian = 0
        l = 0
        r = 0
        maxlength = 0

        while r < len(nums):
            if nums[r] == 1:
                r += 1
            else:
                bian += 1
                r += 1

            while l < r and bian > k:
                maxlength = max(maxlength,r - l-1)
                if nums[l] == 1:
                    l += 1
                else:
                    bian -= 1
                    l += 1

        maxlength = max(maxlength, r - l)
        print(maxlength)
        return maxlength


if __name__ == '__main__':
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2

    # nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    # k = 3

    # nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    # k = 0
    solution = Solution()
    solution.longestOnes(nums,k)