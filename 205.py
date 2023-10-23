class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1 = list()
        t1 = list()

        for i,j in zip(s,t):
            if i not in s1:
                if j not in t1:
                    s1.append(i)
                    t1.append(j)
                else:
                    index = t1.index(j)
                    if s1[index] != i:
                        return False
            else:
                index = s1.index(i)
                if t1[index] !=j:
                    return False

        return True


if __name__ == '__main__':
    # s = "egg"
    # t = "add"
    #
    # s = "foo"
    # t = "bar"
    #
    s = "paper"
    t = "title"
    # s = "badc"
    # t = "baba"
    solution = Solution()
    result = solution.isIsomorphic(s,t)
    print(result)