class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {
            "2":["a","b","c"],
            "3":["d","e","f"],

            "4":["g","h","i"],
            "5":["j","k","l"],


            "6":["m","n","o"],
            "7":["p","q","r","s"],

            "8":["t","u","v"],
            "9":["w","x","y","z"]
        }

        result = []

        digitslength = len(digits)
        if digitslength == 0:
            result = []

        if digitslength == 1:
            result = dic[digits]

        if digitslength == 2:
            for i in range(len(dic[digits[0]])):
                for j in range(len(dic[digits[1]])):
                    # s = dic[digits[0]] + dic[digits[1]]
                    s = dic[digits[0]][i] + dic[digits[1]][j]
                    result.append(s)


        if digitslength == 3:
            for i in range(len(dic[digits[0]])):
                for j in range(len(dic[digits[1]])):
                    for k in range(len(dic[digits[2]])):
                        # s = dic[digits[0]] + dic[digits[1]]
                        s = dic[digits[0]][i] + dic[digits[1]][j] + dic[digits[2]][k]
                        result.append(s)

        if digitslength == 4:
            for i in range(len(dic[digits[0]])):
                for j in range(len(dic[digits[1]])):
                    for k in range(len(dic[digits[2]])):
                        for q in range(len(dic[digits[3]])):
                            # s = dic[digits[0]] + dic[digits[1]]
                            s = dic[digits[0]][i] + dic[digits[1]][j] + dic[digits[2]][k] + dic[digits[3]][q]
                            result.append(s)


        return result









if __name__ == '__main__':
    # digits = "23"
    # digits = ""
    digits = "234"

    solution = Solution()
    result = solution.letterCombinations(digits)

    print(result)