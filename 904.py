class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        res = 0
        left = 0
        right = 0
        have = dict()
        # print(len(have))

        while right < len(fruits):
            if len(have) <= 2:
                if fruits[right] not in have:
                    have[fruits[right]] = 1
                else:
                    have[fruits[right]] += 1

                right += 1
            else:
                tempres = sum(have.values()) - 1
                res = max(tempres,res)
                have[fruits[left]] -= 1
                if have[fruits[left]] == 0:
                    have.pop(fruits[left])
                left += 1
        temp = 0
        if len(have) <= 2:
            temp = sum(have.values())
        else:
            temp = sum(have.values()) - 1

        res = max(temp,res)

        print(res)
        return res





if __name__ == '__main__':
    fruits = [1, 2, 1]
    fruits = [0, 1, 2, 2]
    fruits = [1, 2, 3, 2, 2]
    fruits = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
    fruits = [0,1,2,3,3,2]

    solution = Solution()
    solution.totalFruit(fruits)
    #
    # d = {'a':0,'b':0,'c':1}
    # print(len(d))