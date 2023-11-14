class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        if len(nums) == 1:
            print(nums)
            return nums

        p = 0
        q = len(nums) - 1

        while nums[p] == 0:
            p += 1
            if p == q:
                print(nums)
                return nums
        while nums[q] == 2:
            q -= 1
            if p == q:
                print(nums)
                return nums

        start = p
        end = q+1

        i = start
        while i != q+1:
            if nums[i] == 0:
                temp = nums[i]
                nums[i] = nums[p]
                nums[p] = temp
                p += 1


            elif nums[i] == 2:
                temp = nums[i]
                nums[i] = nums[q]
                nums[q] = temp
                q -= 1



            else:
                i += 1

            while nums[p] == 0:
                p += 1
                i = p
                if p == q:
                    print(nums)
                    return nums
            while nums[q] == 2:
                q -= 1
                if p == q:
                    print(nums)
                    return nums






        print(nums)
        return nums


if __name__ == '__main__':
    nums = [2, 0, 2, 1, 1, 0]
    # nums = [1,2,2,0,0,1,2,0,1]
    nums = [2,2,0,1]
    solution = Solution()
    solution.sortColors(nums)
