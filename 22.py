
# 将（）看作一个整体，见缝插针，找set即可，没用回溯法
# class Solution(object):
#     def generateParenthesis(self, n):
#         """
#         :type n: int
#         :rtype: List[str]
#         """
#         result = list()
#         result.append(['()'])
#         if n == 1:
#             return result[0]
#         # result.append((['()()','(())']))
#         for i in range(1,n):
#             newthing = list()
#             for r in result[i-1]:
#                 # print('rrr',r)
#                 for j in range(len(r)+1):
#                     # print(j)
#                     thing = ''
#                     thing += r[:j]
#                     thing += '()'
#                     thing += r[j:]
#                     # print(thing)
#                     newthing.append(thing)
#
#             newthing = list(set(newthing))
#             result.append(newthing)
#
#
#         print(result)
#         return result[n-1]


#使用回溯法：
'''
！！！！！！！！！！！！！！！！！！！！！
result = []

def traceBack(self,路径,选择列表):
    if 满足结束条件:
        result.add(路径)
        return

    for 选择 in 选择列表:
        做选择
        self.traceBack(路径,选择列表)
        撤销选择

'''


class Solution(object):

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = list()
        self.traceBack([],n,n,result)
        # print(result)
        return result

    def traceBack(self,path,left,right,result):
        if left > right:
            return
        if left < 0 or right < 0:
            return
        if left == 0 and right == 0:
            result.append(''.join(path))
            return

        path.append('(')
        self.traceBack(path,left-1,right,result)
        path.pop(-1)

        path.append(')')
        self.traceBack(path,left,right-1,result)
        path.pop(-1)



if __name__ == '__main__':
    solution = Solution()
    solution.generateParenthesis(3)