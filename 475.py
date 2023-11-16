#超时？ 二分查找
# class Solution(object):
#     def findRadius(self, houses, heaters):
#         """
#         :type houses: List[int]
#         :type heaters: List[int]
#         :rtype: int
#         """
#         houses.sort()
#         heaters.sort()
#         needs = []
#
#         for house in houses:
#             min = pow(10,9)
#             temp = -1
#             for heat in heaters:
#                 temp = abs(house - heat)
#                 if temp <= min:
#                     min = temp
#                 elif temp > min:
#                     break
#             needs.append(min)
#
#         print(needs)
#         print(max(needs))
#         return max(needs)


class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters.append(pow(10,18) + 1)
        heaters.append(pow(-10,18) - 1)
        houses.sort()
        heaters.sort()
        print(heaters)

        ans = list()

        for house in houses:
            left = 0
            right = len(heaters) - 1

            while left < right-1 :
                mid = (left + right) // 2
                if heaters[mid] < house:
                    left = mid
                else:
                    right = mid

            temp = min(abs(heaters[left] - house),abs(heaters[right] - house))
            ans.append(temp)

        print(max(ans))
        return max(ans)








if __name__ == '__main__':
    houses = [1, 2, 3]
    heaters = [2]




    solution = Solution()
    solution.findRadius(houses,heaters)





