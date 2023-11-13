class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        p = 0
        q = 1

        while q < len(nums):
            while nums[q] == nums[p]:
                q += 1
                if q >= len(nums):
                    break
            if q >= len(nums):
                break
            nums[p+1] = nums[q]
            p += 1

        k = p + 1
        print(k,nums)
        return k

if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    nums = [1,1,2]
    solution = Solution()
    solution.removeDuplicates(nums)