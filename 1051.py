class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        maxgoal = 0
        goal = 0

        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                grumpy[i] = 1
            else:
                grumpy[i] = 0
        # print(grumpy)

        l = 0
        r = l + minutes - 1


        while r < len(grumpy):
            if l == 0:
                i = 0
                while i < l:
                    goal += customers[i] * grumpy[i]
                    i+=1
                while i <= r:
                    goal += customers[i] * 1
                    i+=1
                while i < len(customers):
                    goal += customers[i] * grumpy[i]
                    i+=1
            else:
                if grumpy[l-1] == 1:
                    goal -= 0
                else:
                    goal -= customers[l-1]
                if grumpy[r] == 1:
                    goal += 0
                else:
                    goal += customers[r]


            maxgoal = max(goal,maxgoal)


            l += 1
            r += 1

        print(maxgoal)
        return maxgoal



if __name__ == '__main__':
    customers = [1, 0, 1, 2, 1, 1, 7, 5]
    grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
    minutes = 3


    # customers = [1]
    # grumpy = [0]
    # minutes = 1
    solution = Solution()
    solution.maxSatisfied(customers,grumpy,minutes)