# 超时了！！！！我的一个小时啊！！！！！
# class Solution(object):
#     def numberOfSubarrays(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         totaoji = 0
#         for num in nums:
#             if num % 2 == 1:
#                 totaoji += 1
#         # print(totaoji)
#         if totaoji < k:
#             print(0)
#             return 0
#
#         i = 0
#         res = 0
#         currk = 0
#
#         while i < len(nums):
#             j = i
#             while j < len(nums):
#                 if nums[j] % 2 == 1:
#                     currk += 1
#                     break
#                 j += 1
#
#             l = j - i + 1
#
#             q = j + 1
#
#             while q < len(nums) and currk < k:
#                 if nums[q] % 2 == 1:
#                     currk += 1
#                 q += 1
#
#             p = q
#
#             while p < len(nums) and nums[p] % 2 == 0:
#                 p += 1
#             r = p - q + 1
#
#             if currk < k:
#                 r = 0
#
#
#             res += l * r
#
#             i = j + 1
#             currk = 0
#
#         print(res)
#         return res


class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        totaoji = 0
        for num in nums:
            if num % 2 == 1:
                totaoji += 1
        # print(totaoji)
        if totaoji < k:
            print(0)
            return 0

        jilist = list()
        # jilist.append(-1)
        for index in range(len(nums)):
            if nums[index] % 2 == 1:
                jilist.append(index)
        # jilist.append(len(nums))
        print(jilist)

        l = 0
        r = 0 + k - 1
        res = 0

        while r < len(jilist):
            if l == 0:
                zuo = jilist[l] + 1
            else:
                zuo = jilist[l] - jilist[l-1]
            if r == len(jilist) - 1:
                you = len(nums) - jilist[r]
            else:
                you = jilist[r+1] - jilist[r]
            # print("jilist[l],jilist[r]",jilist[l],jilist[r])
            # print("zuo,you",zuo,you)
            res += zuo * you
            l += 1
            r += 1

        print(res)
        return res














if __name__ == '__main__':
    nums = [1, 1, 2, 1, 1]
    k = 3

    nums = [2, 4, 6]
    k = 1

    nums = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2]
    k = 2

    nums = [2,2,2,1,2,2,1,2,2,2,1,2,2,2]
    k = 2

    nums = [1,1,1,1,1]
    k = 1
    solution = Solution()
    solution.numberOfSubarrays(nums,k)