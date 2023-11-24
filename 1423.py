class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        k1 = len(cardPoints) - k
        l = 0
        r = l + k1 - 1
        sum1 = sum(cardPoints[l:r+1])
        minsum = sum(cardPoints[l:r+1])
        # print(minsum)

        while r < len(cardPoints):
            if l == 0:
                sum1 = sum(cardPoints[l:r+1])
            else:
                sum1 += cardPoints[r]
                sum1 -= cardPoints[l-1]

            minsum = min(minsum,sum1)
            l += 1
            r += 1


        print(minsum)
        print(sum(cardPoints))
        print(sum(cardPoints) - minsum)
        return sum(cardPoints) - minsum



if __name__ == '__main__':
    cardPoints = [1, 2, 3, 4, 5, 6, 1]
    k = 3

    cardPoints = [56,27,75,44,38,78,12,43,2,57,71,30,78,38,60,81,61,7,23,85,28,41,47]
    k = 2
    s = Solution()
    s.maxScore(cardPoints, k)
