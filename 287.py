class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p = 0
        for p in range(len(nums)):
            for q in range(p+1,len(nums)):
                # print(p,q)
                if nums[p] == nums[q]:
                    print(nums[p])
                    return nums[p]


if __name__ == '__main__':
    nums = [1, 3, 4, 2, 2]
    nums = [3, 1, 3, 4, 2]
    solution = Solution()
    solution.findDuplicate(nums)