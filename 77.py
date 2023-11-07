#因为创建了数组而超时？？？？
# class Solution(object):
#     def combine(self, n, k):
#         """
#         :type n: int
#         :type k: int
#         :rtype: List[List[int]]
#         """
#
#         results = list()
#         nums = list()
#
#         for i in range(1,n+1):
#             nums.append(i)
#         # print(nums[:])
#
#         self.traceBack(nums[:],k,[],results)
#
#         re = list()
#         for r in results:
#             r.sort()
#             if r not in re:
#                 re.append(r)
#         print(re)
#
#
#
#         return re
#
#     def traceBack(self,nums,k,path,results):
#         if len(path) == k:
#             results.append(path[:])
#             return
#
#         for index,num in enumerate(nums):
#             nums.pop(index)
#             path.append(num)
#
#             self.traceBack(nums[index:],k,path,results)
#
#             nums.insert(index,num)
#             path.pop(-1)



class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        results = list()
        self.traceBack(n,k,1,[],results)

        print(results)
        return results

    def traceBack(self,n,k,begin,path,results):
        if len(path) == k:
            results.append(path[:])
            return

        for i in range(begin,n+1):
            path.append(i)
            self.traceBack(n,k,i+1,path,results)
            path.pop(-1)

if __name__ == '__main__':
    # n = 4
    # k = 2

    # n = 13
    # k = 13

    n = 20
    k = 10
    solution = Solution()
    solution.combine(n,k)
