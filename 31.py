class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        length = len(nums)
        if length == 1:
            print(nums)
            return nums
        else:
            p = length - 2
            q = length - 1

            while p != -1:
                q = length - 1

                if nums[p] < nums[q]:
                    temp = nums[q]
                    nums[q] = nums[p]
                    nums[p] = temp
                    j = len(nums) - 1
                    for i in range(p+1,int((len(nums) + p + 1) /2)):

                        temp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = temp

                        j -= 1
                    print(nums)
                    return nums

                else:
                    while p != q:
                        q -= 1

                        if nums[p] < nums[q]:
                            temp = nums[q]
                            nums[q] = nums[p]
                            nums[p] = temp
                            j = len(nums) - 1
                            for i in range(p + 1, int((len(nums) + p + 1) / 2)):
                                temp = nums[i]
                                nums[i] = nums[j]
                                nums[j] = temp

                                j -= 1
                            print(nums)
                            return nums



                p -= 1

            j = len(nums) - 1
            for i in range(p + 1, int((len(nums) + p + 1) / 2)):
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp

                j -= 1
            print(nums)
            return nums


if __name__ == '__main__':
    nums = [3,2,1]
    solution = Solution()
    solution.nextPermutation(nums)