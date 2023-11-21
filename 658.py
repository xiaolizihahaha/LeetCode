import copy


class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        if x < arr[0]:
            print(arr[:k])
            return arr[:k]
        elif x > arr[-1]:
            print(arr[len(arr)-k:])
            return arr[len(arr)-k:]
        else:
            left = 0
            right = k - 1
            minsum1 = 0

            for i in range(left,right+1):
                minsum1 += abs(arr[i]-x)
            # print(minsum1)

            sum1 = minsum1
            res = arr[left:right+1]

            while left < len(arr) - k:
                # print(left)
                sum1 -= abs(arr[left] - x)
                sum1 += abs(arr[right + 1] - x)

                if sum1 < minsum1:
                    minsum1 = sum1
                    # print(sum1,arr[left+1:right+2])
                    res = arr[left+1:right+2]

                left += 1
                right += 1

            print(res)
            print(minsum1)
            return res







if __name__ == '__main__':
    arr = [1,2,3,4,5]
    k = 4
    x = 4

    # arr = [1, 2, 3, 4, 5]
    # k = 4
    # x = -1

    # arr = [1,1,1,10,10,10]
    # k = 1
    # x = 9
    solution = Solution()
    solution.findClosestElements(arr,k,x)