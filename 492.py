class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        ans = list()

        if pow(area,0.5) % 1 == 0:
            ans.append(int(pow(area,0.5)))
            ans.append(int(pow(area, 0.5)))
            print(ans)
            return ans

        else:
            mid = int(pow(area,0.5))
            i = mid
            while i >= 1:
                if area % i == 0:

                    ans.append(int(area/i))
                    ans.append(i)
                    print(ans)
                    return ans
                i -= 1




if __name__ == '__main__':
    # print(pow(9,0.5) % 1 == 0)
    solution = Solution()
    solution.constructRectangle(pow(10,7))