class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        p = -1
        q = 0

        while q < len(nums):
            if nums[q] != val:
                nums[p+1] = nums[q]
                p += 1
                q += 1
            else:
                while nums[q] == val:
                    q += 1
                    if q >= len(nums):
                        break
        k = p+1
        print(k,nums)
        return k

if __name__ == '__main__':
    # nums = [3, 2, 2, 3]
    # val = 3
    #
    # nums = [0, 1, 2, 2, 3, 0, 4, 2]
    # val = 2
    solution = Solution()
    solution.removeElement(nums,val)