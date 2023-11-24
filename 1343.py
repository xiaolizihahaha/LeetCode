class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        res = 0

        l = 0
        r = l + k - 1
        sum1 = 0

        while r < len(arr):
            if l == 0:
                sum1 = sum(arr[l:r+1])
            else:
                sum1 += arr[r]
                sum1 -= arr[l - 1]

            if sum1 / k >= threshold:
                res += 1


            l += 1
            r += 1


        print(res)
        return res


if __name__ == '__main__':
    arr = [2, 2, 2, 2, 5, 5, 5, 8]
    k = 3
    threshold = 4
    # 3
    #
    arr = [11, 13, 17, 23, 29, 31, 7, 5, 2, 3]
    k = 3
    threshold = 5
    # 6

    solution = Solution()
    solution.numOfSubarrays(arr, k, threshold)