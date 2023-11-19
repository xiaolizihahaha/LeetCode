class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        slist = s.split(' ')
        print(slist)
        news = ''
        for index,ss in enumerate(slist):
            news += ss[::-1]

            if index != len(slist)-1:
                news += ' '

        print(news)
        return news


if __name__ == '__main__':
    s = "Let's take LeetCode contest"
    # s = "God Ding"

    solution = Solution()
    solution.reverseWords(s)