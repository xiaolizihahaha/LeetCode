class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        ans = -1

        while left <= right:
            mid = (left + right) // 2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1

            if count <= mid:
                left = mid + 1
            else:
                right = mid - 1
                ans = mid

        print(ans)
        return ans



if __name__ == '__main__':
    nums = [1, 3, 4, 2, 2]
    # nums = [3, 1, 3, 4, 2]
    solution = Solution()
    solution.findDuplicate(nums)