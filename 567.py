class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1list = list(s1)
        s1list.sort()
        news1 = ''.join(s1list)
        print(news1)

        i = 0

        while i < len(s2) - len(s1) + 1:
            if s2[i] in s1:
                temp = s2[i:i+len(s1)]
                templist = list(temp)
                templist.sort()
                news2str = ''.join(templist)

                if news2str == news1:
                    print(1)
                    return True

            i += 1
        print(0)
        return False







if __name__ == '__main__':
    s1 = "ab"
    s2 = "eidbaooo"

    s1 = "ab"
    s2 = "eidboaoo"

    s1 = 'adc'
    s2 = "dcda"


    solution = Solution()
    solution.checkInclusion(s1,s2)