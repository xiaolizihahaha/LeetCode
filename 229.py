class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        numdic = dict()
        numList = list()
        for num in nums:
            if numdic.get(num) is None:
                numdic[num] = 0
            numdic[num] += 1
        print(numdic)

        for num, val in numdic.items():
            if val > int(len(nums) / 3):
                numList.append(num)
        return numList

if __name__ == '__main__':
    # nums = [3, 2, 3]
    nums = [1]
    nums = [1,2]
    solution = Solution()
    result = solution.majorityElement(nums)
    print(result)