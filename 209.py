# # 暴力求解超时
# class Solution(object):
#     def minSubArrayLen(self, target, nums):
#         """
#         :type target: int
#         :type nums: List[int]
#         :rtype: int
#         """
#         minlenth = len(nums) + 1
#         for index,num in enumerate(nums):
#             sum = 0
#             i = 0
#             while index + i < len(nums):
#                 sum += nums[index + i]
#                 if sum >= target:
#                     break
#                 else:
#                     i += 1
#             if sum >= target:
#                 lenth = i + 1
#                 if lenth <= minlenth:
#                     minlenth = lenth
#
#         if minlenth == len(nums) + 1:
#             print(0)
#             return 0
#         else:
#             print(minlenth)
#             return minlenth

# 滑动窗口
# class Solution(object):
#     def minSubArrayLen(self, target, nums):
#         """
#         :type target: int
#         :type nums: List[int]
#         :rtype: int
#         """
#         minlenth = len(nums) + 1
#
#         start = 0
#         end = 0
#         sum = 0
#
#         while start < len(nums) and end < len(nums):
#             sum += nums[end]
#             if sum < target:
#                 end += 1
#             else:
#                 lenth = end - start + 1
#                 if minlenth > lenth:
#                     minlenth = lenth
#                 sum -= nums[start]
#                 sum -= nums[end]
#                 start += 1
#
#
#
#         if minlenth == len(nums) + 1:
#             print(0)
#             return 0
#         else:
#             print(minlenth)
#             return minlenth


# 滑动窗口
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) < target:
            return 0
        left = 0
        right = 0
        sum1 = 0
        minlength = len(nums) + 1

        while right < len(nums):
            sum1 += nums[right]
            right += 1

            while left < right and sum1 >= target:
                length = right - left
                minlength = min(minlength, length)

                sum1 -= nums[left]
                left += 1

        return minlength



if __name__ == '__main__':
    # target = 7
    # nums = [2, 3, 1, 2, 4, 3]
    #
    # target = 4
    # nums = [1, 4, 4]
    #
    target = 11
    nums = [1, 1, 1, 1, 1, 1, 1, 1]
    solution = Solution()
    solution.minSubArrayLen(target,nums)