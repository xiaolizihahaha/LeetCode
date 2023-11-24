class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        l = 0
        r = 0
        length = 0
        maxlength = 0
        qianmin = nums[0]
        qianmax = nums[0]

        while r < len(nums):
            qianmax = max(qianmax,nums[r])
            qianmin = min(qianmin,nums[r])
            r += 1


            if r == len(nums):
                break
            if l != r:
                snums = sorted(nums[l:r])
                while l < r and max(abs(max(nums[l:r]) - nums[r]),abs(min(nums[l:r]) - nums[r])) > limit:
                    length = r - l
                    maxlength = max(maxlength,length)
                    l += 1
        k = len(nums) - 1
        if max(abs(max(nums[l:k+1]) - nums[k]), abs(min(nums[l:k+1]) - nums[k])) <= limit:
            length = k - l + 1
        maxlength = max(maxlength, length)

        print(maxlength)
        return maxlength




if __name__ == '__main__':
    nums = [8, 2, 4, 7]
    limit = 4

    nums = [10, 1, 2, 4, 7, 2]
    limit = 5
    #
    # nums = [4, 2, 2, 2, 4, 4, 2, 2]
    # limit = 0
    s = Solution()
    s.longestSubarray(nums, limit)