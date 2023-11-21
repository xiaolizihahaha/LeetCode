# class Solution(object):
#     def findMaxAverage(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: float
#         """
#         if len(nums) == 1:
#             print(nums[0] / 1)
#             return nums[0] / 1.0
#         else:
#             left = 0
#             right = left + k - 1
#             sum1 = sum(nums[left:right+1])
#             print(sum1)
#             maxaverge = sum1 * 1.0 / k
#
#             while left < len(nums) - k:
#                 # print(left)
#                 sum1 = sum1 - nums[left] + nums[right+1]
#                 averge = sum1 * 1.0 / k
#
#                 if averge > maxaverge:
#                     maxaverge = averge
#                 left += 1
#                 right += 1
#
#             print(maxaverge)
#             return maxaverge


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        left = 1
        right = 1 + k - 1
        maxaverge = sum(nums[0:k]) * 1.0 / k
        sum1 = sum(nums[0:k])
        print(sum1)

        while right < len(nums):

            sum1 += nums[right]
            sum1 -= nums[left-1]
            print(sum1)
            maxaverge = max(sum1 * 1.0 / k,maxaverge)
            right += 1
            left += 1
        print(maxaverge)
        return maxaverge


if __name__ == '__main__':
    nums = [1, 12, -5, -6, 50, 3]
    k = 4

    # nums = [5]
    # k = 1

    # nums = [3, 3, 4, 3, 0]
    # k = 3
    #
    # nums = [4,0,4,3,30]
    # k = 3
    solution = Solution()
    solution.findMaxAverage(nums,k)