# timeout
# class Solution(object):
#     def replaceElements(self, arr):
#         """
#         :type arr: List[int]
#         :rtype: List[int]
#         """
#         res = []
#         for index in range(len(arr) - 1):
#             l = index + 1
#             r = len(arr) - 1
#
#             while l < r:
#                 if arr[l] < arr[r]:
#                     l += 1
#                 else:
#                     r -= 1
#             res.append(arr[l])
#
#         res.append(-1)
#         print(res)
#         return res

# timeout
# class Solution(object):
#     def replaceElements(self, arr):
#         """
#         :type arr: List[int]
#         :rtype: List[int]
#         """
#         res = []
#         for index in range(len(arr)):
#             if index != len(arr) - 1:
#                 res.append(max(arr[index + 1:]))
#             else:
#                 res.append(-1)
#
#         return res



class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        res = [-1] * len(arr)
        i = len(arr) - 2
        while i >= 0:
            res[i] = max(res[i+1],arr[i+1])
            i -= 1

        print(res)
        return res


if __name__ == '__main__':
    solution = Solution()
    solution.replaceElements(arr=[17,18,5,4,6,1])
