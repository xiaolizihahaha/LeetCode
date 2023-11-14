class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        if n == 0:
            print(nums1)
            return

        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            print(nums1)
            return

        else:
            p = m - 1
            q = n - 1
            k = m + n - 1

            while p >= 0 and q >= 0:
                if nums1[p] < nums2[q]:
                    nums1[k] = nums2[q]
                    q -= 1
                    k -= 1
                else:
                    nums1[k] = nums1[p]
                    p -= 1
                    k -= 1
            while q >= 0:
                nums1[k] = nums2[q]
                q -= 1
                k -= 1
            while p >= 0:
                nums1[k] = nums1[p]
                p -= 1
                k -= 1

            print(nums1)
            return




if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    # nums1 = [1]
    # m = 1
    # nums2 = []
    # n = 0

    # nums1 = [0]
    # m = 0
    # nums2 = [1]
    # n = 1
    solution = Solution()
    solution.merge(nums1,m,nums2,n)