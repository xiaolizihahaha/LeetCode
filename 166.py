class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """

        result = ''
        yushu = []
        index = -1
        fuhao = 1
        up = numerator
        down = denominator


        if numerator < 0 and denominator < 0:
            fuhao = 1
            up = 0 - numerator
            down = 0 - denominator


        if numerator < 0 and denominator > 0:
            fuhao = -1
            up = 0 - numerator
            down = denominator


        if numerator > 0 and denominator < 0:
            fuhao = -1
            up = numerator
            down = 0 - denominator




        result += str(int(up / down))
        up = up % down

        if up == 0:
            if fuhao == 1:
                return result
            else:
                return '-' + result

        else:
            result += '.'
            yushu.append(up)

            while up % down != 0:
                up = up * 10
                result += str(int(up /down))
                up = up % down
                if up in yushu:
                    index = yushu.index(up)
                    break
                yushu.append(up)
            if index != -1:

                index1 = result.index('.')
                result1 = result[:index1 + index + 1] + '(' + result[index1 + index + 1:] + ')'

                if fuhao == 1:
                    return result1
                else:
                    return '-' + result1

            if fuhao == 1:
                return result
            else:
                return '-' + result



if __name__ == '__main__':

    # numerator = 1
    # denominator = 2
    # # 0.5




    #
    # numerator = 0.25
    # denominator = 5
    # 2
    #
    numerator = -50
    denominator = 8
    # numerator = 4
    # denominator = 333

    # # "0.(012)"


    solution = Solution()
    result = solution.fractionToDecimal(numerator,denominator)
    print(result)
