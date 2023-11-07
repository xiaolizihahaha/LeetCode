# import math
#timeout 超时

# class Solution(object):
#     def grayCode(self, n):
#         """
#         :type n: int
#         :rtype: List[int]
#         """
#         path = list()
#         origin = [0] * n
#         path.append(origin)
#         cur = origin
#
#         self.traceBack(n,path,cur)
#         print(path)
#
#         re = list()
#         for s in path:
#             num = int(s,2)
#             re.append(num)
#
#         print(re)
#         return re
#
#     def traceBack(self,n,path,cur):
#         if len(path) == int(math.pow(2,n)):
#             return
#
#
#         for i in range(len(cur)):
#             if cur[i] == '0':
#                 cur
#             elif cur[i] == '1':
#                 newstr = cur[:i] + '0' + cur[i + 1:]
#             if newstr not in path:
#                 path.append(newstr)
#                 self.traceBack(n,path,newstr)
#                 break

#另一种思路：
import math
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        path = list()
        self.traceBack(n,path,'',0)
        print(path)
        return path

    def traceBack(self,n,path,cur,x):
        if len(cur) == n:
            # print(len(cur))
            path.append(int(cur,2))
            return

        if x == 0:
            self.traceBack(n,path,cur+'0',0)
            self.traceBack(n,path,cur+'1',1)
        elif x == 1:
            self.traceBack(n,path,cur+'1',0)
            self.traceBack(n,path,cur+'0',1)






if __name__ == '__main__':
    solution = Solution()
    solution.grayCode(2)

