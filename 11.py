class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(height) - 1
        volume = 0

        while start != end:
            temp = min(height[start],height[end]) * (end - start)
            # print(temp)
            if temp > volume:
                volume = temp

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        print(volume)
        return volume


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    height = [1, 1]

    solution = Solution()
    solution.maxArea(height)