class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return

        p = 0
        q = 0

        while p < len(nums):
            while 1:
                if p >= len(nums) or nums[p] != 0:
                    break
                p += 1
            if p >= len(nums):
                break

            while 1:
                if q >= len(nums) or nums[q] == 0:
                    break
                q += 1
            if q >= len(nums):
                break

            if q < p:
                temp = nums[p]
                nums[p] = nums[q]
                nums[q] = temp
            else:
                p += 1

        print(nums)

if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    nums = [0,0,1,0,2,3,0,0,4,5,3,0,0]

    nums = [1,3,0,12,0]
    solution = Solution()
    solution.moveZeroes(nums)

