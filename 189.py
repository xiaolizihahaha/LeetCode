class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        total = k

        temp = list()
        for i in range(len(nums)-k,len(nums)):
            temp.append(nums[i])

        i = len(nums) - 1
        while i >= k:
            nums[i] = nums[i-k]
            i -= 1

        for i in range(0,k):
            nums[i] = temp[i]


        print(nums)



if __name__ == '__main__':
    # nums = [1, 2, 3, 4, 5, 6, 7]
    # k = 3
    #
    # nums = [-1, -100, 3, 99]
    # k = 2
    #
    nums = [1, 2]
    k = 3
    solution = Solution()
    solution.rotate(nums,k)