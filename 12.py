class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        chList = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        numList = [1000,900,500,400,100,90,50,40,10,9,5,4,1]

        result = ""
        last = num

        while last != 0 :

            index = -1
            for n in numList:
                if last < n :
                    continue
                else :
                    index = numList.index(n)
                    if index != -1 :
                        result += chList[index]
                        last -= n
                        break



        return result





if __name__ == '__main__':
    # num = 3
    # num = 4
    # num = 9
    # num = 58
    num = 1994


    solution = Solution()
    result = solution.intToRoman(num)



    print(result)