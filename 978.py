class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        l = 0
        r = 0
        maxlength = 1
        length = 1

        while r+1 < len(arr):
            if l == r:
                r += 1
            else:
                if arr[r-1] > arr[r] and arr[r] < arr[r+1] or arr[r-1] < arr[r] and arr[r] > arr[r+1]:
                    r += 1
                else:
                    if arr[r-1] != arr[r] or arr[r] != arr[r+1]:
                        maxlength = max(maxlength,r-l+1)
                    else:
                        maxlength = max(maxlength, r - l)
                    l += 1

        if arr[r] != arr[r-1]:
            length = r - l + 1
        if arr[r] == arr[r-1]:
            length = r - l
        maxlength = max(maxlength, length)
        print(maxlength)
        return maxlength

if __name__ == '__main__':
    arr = [9, 4, 2, 10, 7, 8, 8, 1, 9]
    # 输出：5

    arr = [4, 8, 12, 16]
    # 输出：2

    arr = [1,2,1,2,1,1,1,3,2,5,2,6]



    solution = Solution()
    solution.maxTurbulenceSize(arr)