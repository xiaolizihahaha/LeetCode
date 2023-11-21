# class Solution(object):
#     def numSubarrayProductLessThanK(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#
#         if k == 0:
#             return 0
#
#         left = 0
#         right = 0
#         cheng = nums[0]
#         res = 0
#
#         while left < len(nums):
#
#             while cheng < k:
#                 if right + 1 < len(nums):
#                     right += 1
#                     cheng = cheng * nums[right]
#                 else:
#                     res += right - left + 1
#                     cheng = cheng / nums[left]
#                     left += 1
#                     if left >= len(nums):
#                         break
#
#             if cheng >= k:
#                 if right - left >= 0:
#                     res += right - left
#                 else:
#                     res += 0
#                 if right < left:
#                     right = left
#                     cheng = nums[left]
#                 else:
#                     cheng = cheng / nums[left]
#                     left += 1
#
#         print(res)
#         if res < 0:
#             return 0
#         else:
#             return res


class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        right = 0
        cheng = 1
        res = 0

        while right < len(nums):
            cheng *= nums[right]
            right += 1
            while left < right and cheng >= k:
                cheng = cheng / nums[left]
                left += 1
            res += right - left + 1

        return res








if __name__ == '__main__':
    #
    # nums = [1,1,1]
    # k = 1
    # #
    # # nums = [57, 44, 92, 28, 66, 60, 37, 33, 52, 38, 29, 76, 8, 75, 22]
    # # k = 18
    #
    # nums = [10, 5, 2, 6]
    # k = 100
    # # 8
    #
    # nums = [1, 2, 3]
    # k = 0
    # # 0
    #
    # nums = [10,9,10,4,3,8,3,3,6,2,10,10,9,3]
    # k = 19


    nums = [1,2,3,4,5]
    k = 1


    solution = Solution()
    solution.numSubarrayProductLessThanK(nums,k)