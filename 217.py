class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numdic = dict()
        for num in nums:
            if numdic.get(num) is None:
                numdic[num] = 0
            numdic[num] += 1
            if numdic[num] >= 2:
                return True
        return False





if __name__ == '__main__':

    # nums = [1, 2, 3, 1]
    # 输出：true

    # nums = [1, 2, 3, 4]
    # 输出：false

    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    # 输出：true

    solution = Solution()
    result = solution.containsDuplicate(nums)
    print(result)