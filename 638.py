class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """

        results = list()
        results.append(0)
        for i in range(len(price)):
            results[0] += price[i] * needs[i]

        # print(results[0])
        avoid = list()
        for i in range(len(special)):
            s = 0
            for j in range(len(price)):
                s += special[i][j] * price[j]
            print(s)
            if special[i][-1] >= s:
                avoid.append(i)

        avoid.reverse()
        print(avoid)
        for i in avoid:
            special.pop(i)



                # print(special[i][j])
                # print(price[j])
            # if s > special[i][-1]:
            #     special.pop(i)




        self.dfs(price,special,needs,0,results)

        print(results[0])
        return results[0]


    def dfs(self,price,special,needs,sums,results):
        if needs.count(0) == len(needs):
            # print('sums',sums)
            if sums < results[0]:
                # print('aaaa',sums)
                results[0] = sums
            return

        for s in special:
            enough = True
            needs2 = list()
            for i in range(len(needs)):
                needs2.append(needs[i] - s[i])
                if needs[i] < s[i]:
                    enough = False
                    break

            if enough is True:
                # for i in range(len(needs)):
                #     needs[i] = needs[i] - s[i]
                sums = sums + s[-1]

                self.dfs(price,special,needs2,sums,results)
                #
                # for i in range(len(needs)):
                #     needs[i] = needs[i] + s[i]
                sums = sums - s[-1]

        for i in range(len(needs)):
            sums += needs[i] * price[i]

        self.dfs(price,special,[0] * len(needs),sums,results)




if __name__ == '__main__':
    price = [2, 5]
    special = [[3, 0, 5],
               [1, 2, 10]]
    needs = [3, 2]


    # price = [2, 3, 4]
    # special = [[1, 1, 0, 4],
    #            [2, 2, 1, 9]]
    # needs = [1, 2, 1]
    solution = Solution()
    solution.shoppingOffers(price,special,needs)


