class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsd = dict()
        l = 0
        r = 0
        maxsum = 0
        sum1 = 0

        while r < len(nums):
            if nums[r] not in numsd:
                numsd[nums[r]] = 1
                sum1 += nums[r]
                r += 1
            else:
                while l < r:
                    maxsum = max(maxsum,sum1)
                    numsd[nums[l]] -= 1
                    numsd.pop(nums[l])
                    sum1 -= nums[l]
                    if nums[l] == nums[r]:
                        l += 1
                        break
                    l += 1
        maxsum = max(maxsum, sum1)
        print(maxsum)
        return maxsum




if __name__ == '__main__':
    nums = [4, 2, 4, 5, 6]
    nums = [5, 2, 1, 2, 5, 2, 1, 2, 5]
    nums = [1,2,3,2,2,2,1,3,4]
    nums = [187,470,25,436,538,809,441,167,477,110,275,133,666,345,411,459,490,266,987,965,429,166,809,340,467,318,125,165,809,610,31,585,970,306,42,189,169,743,78,810,70,382,367,490,787,670,476,278,775,673,299,19,893,817,971,458,409,886,434]
    solution = Solution()
    solution.maximumUniqueSubarray(nums)