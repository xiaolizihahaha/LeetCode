class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        print(nums)
        res = 0

        for index, num in enumerate(nums[:len(nums)-1]):
            if index != 0 and nums[index] == nums[index - 1]:
                continue

            target = num + k
            left = index + 1
            right = len(nums) - 1
            while left < right - 1:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid-1
                else:
                    left = mid

            if nums[left] == target or nums[right] == target:
                res += 1


        print(res)
        return res




if __name__ == '__main__':
    # nums = [3, 1, 4, 1, 5]
    # k = 2

    nums = [1, 2, 3, 4, 5]
    k = 1
    #
    nums = [1, 3, 1, 5, 4]
    k = 0
    solution = Solution()
    solution.findPairs(nums,k)