class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        total = 0
        if len(timeSeries) == 1:
            total += duration
            return total

        else:
            for i in range(len(timeSeries) - 1):
                if timeSeries[i] + duration > timeSeries[i+1]:
                    total += timeSeries[i+1] - timeSeries[i]
                else:
                    total += duration
            total += duration
            print(total)
            return total

if __name__ == '__main__':
    timeSeries = [1, 4]
    duration = 2

    timeSeries = [1, 3, 7]
    duration = 3

    solution = Solution()
    solution.findPoisonedDuration(timeSeries,duration)

