# class Solution(object):
#     def canReach(self, s, minJump, maxJump):
#         """
#         :type s: str
#         :type minJump: int
#         :type maxJump: int
#         :rtype: bool
#         """
#         temp = [0] * len(s)
#         temp[0] = 1
#
#         for i in range(len(s)):
#             if temp[i] == 1:
#                 if i == 0:
#                     for j in range(minJump,maxJump+1):
#                         if i + j < len(s) and s[i + j] == '0':
#                             temp[i+j] = 1
#                 else:
#                     for j in range(2 * minJump,minJump + maxJump+1):
#                         if i + j < len(s) and s[i + j] == '0':
#                             temp[i+j] = 1
#
#
#         print(temp)
#         if temp[-1] == 1:
#             return True
#         else:
#             return False

#还是不行
class Solution(object):
    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        temp = [0] * len(s)
        temp[0] = 1

        l = 0
        r = 0

        while r < len(s) and l < len(s):
            while  l < len(s) and temp[l] != 1:
                l += 1
            while r > l and temp[r] != 1:
                r -= 1
            left = min(l+minJump,len(s))
            right = min(r+maxJump+1,len(s))

            for i in range(left,right):
                temp[i] = int(s[i]) ^ 1
            if temp[left:right].count(0) == right - left:
                return False
            # temp[left:right] = [int(i)^1 for i in s[left:right] if i == 0]
            l = left
            r = right - 1
            if r == len(s) - 1:
                break
        print(temp)
        return temp[-1] == 1



if __name__ == '__main__':
    s = "011010"
    minJump = 2
    maxJump = 3

    # s = "0100010"
    # minJump = 2
    # maxJump = 3

    s = "01101110"
    minJump = 2
    maxJump = 3
    solution = Solution()
    solution.canReach(s, minJump, maxJump)