class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        numList = (length+1) * [0]

        for num in nums:
            numList[num] = 1

        # print(numList)

        for i in range(length+1):
            if numList[i] == 0:
                return i

if __name__ == '__main__':
    nums = [3, 0, 1]
    # nums = [0, 1]
    # nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    # nums = [0]
    solution = Solution()
    result = solution.missingNumber(nums)
    print(result)
