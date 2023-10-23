class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = int(len(nums) / 2)
        dicNum = dict()
        for num in nums:
            if dicNum.get(num) is None:
                dicNum[num] = 1
            else:
                dicNum[num] += 1
            if dicNum[num] > length:
                return num

if __name__ == '__main__':
    nums = [3, 2, 3]
    nums = [2, 2, 1, 1, 1, 2, 2]

    solution = Solution()
    result = solution.majorityElement(nums)
    print(result)