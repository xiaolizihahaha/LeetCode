import copy


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s1 = copy.deepcopy(s)
        s1 += ' '
        number = 0

        chList = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        numList = [1000,900,500,400,100,90,50,40,10,9,5,4,1]

        slength = len(s)

        i = 0

        while i < slength:
            if chList.count(s1[i:i+2]) != 0:
                number += numList[chList.index(s1[i:i + 2])]
                i += 2
                continue
            if chList.count(s1[i:i+1]) != 0:
                number += numList[chList.index(s1[i:i + 1])]
                i += 1
                continue

        return number

if __name__ == '__main__':

    # s = "III"
    # s = "IV"
    # s = "IX"
    # s = "LVIII"
    s = "MCMXCIV"

    solution = Solution()
    result = solution.romanToInt(s)
    print(result)