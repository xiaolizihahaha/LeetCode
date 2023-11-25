class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsl = []
        i = 0
        index = 0



        while index < len(nums):
            if nums[index] == 0:
                numsl.append(0)
                index += 1
            else:
                i = 0
                while index < len(nums) and nums[index] != 0:
                    i += 1
                    index += 1
                numsl.append(i)

        # print(numsl)

        if numsl.count(0) == 0:
            print(numsl[0]-1)
            return numsl[0] - 1

        if numsl.count(0) == len(numsl):
            print(0)
            return 0

        l = 0
        r = 0
        maxres = 0
        count0 = 0

        while r < len(numsl):
            if numsl[r] == 0:
                count0 += 1
            r += 1

            while l < r and count0 > 1:
                maxres = max(maxres,sum(numsl[l:r]))
                if numsl[l] == 0:
                    count0 -= 1
                l += 1

        maxres = max(maxres, sum(numsl[l:r]))

        print(maxres)
        return maxres







if __name__ == '__main__':
    nums = [1, 1, 0, 1]
    nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]

    nums = [1,1,0,1,1,1,0,1,1,0,1,1,1,1,1,1,0,0,1,1,1,0,1,1,1,1,1,1,1,1,1]
    # nums = [1,1,1]
    solution = Solution()
    solution.longestSubarray(nums)