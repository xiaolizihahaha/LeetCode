from sortedcontainers import SortedList
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

        s = SortedList()
        s.add(nums[l])

        while r < len(nums):
            r += 1


            if r == len(nums):
                break
            if l != r:
                # snums = sorted(nums[l:r])

                while l < r and max(abs(s[0] - nums[r]),abs(s[-1] - nums[r])) > limit:
                    length = r - l
                    maxlength = max(maxlength,length)
                    s.remove(nums[l])

                    l += 1
            s.add(nums[r])

        k = len(nums) - 1
        s.add(nums[k])

        if max(abs(s[0] - nums[k]), abs(s[-1] - nums[k])) <= limit:
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