class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        slist = list()
        news = ''
        i = 0
        while i != len(s):
            j = 0
            str = ''
            while j < k and i + j <len(s):
                str += s[i+j]
                j += 1
            slist.append(str)
            i = i+j

        print(slist)

        for i in range(len(slist)):
            if i % 2 == 0:
                news += slist[i][::-1]
            else:
                news += slist[i]

        print(news)
        return news



if __name__ == '__main__':
    s = "abcdefg"
    k = 2
    # 输出："bacdfeg"

    s = "abcd"
    k = 2
    # 输出："bacd"
    solution = Solution()
    solution.reverseStr(s,k)