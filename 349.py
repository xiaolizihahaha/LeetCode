class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        res = list()
        p = 0
        q = 0

        nums1.sort()
        nums2.sort()
        print(nums1,nums2)

        while p < len(nums1) and q < len(nums2):
            if nums1[p] == nums2[q]:
                if nums1[p] not in res:
                    res.append(nums1[p])
                p += 1
                q += 1


            elif nums1[p] < nums2[q]:
                while p < len(nums1) and nums1[p] < nums2[q]:
                    p += 1


            elif nums1[p] > nums2[q]:
                while q < len(nums2) and nums1[p] > nums2[q]:
                    q += 1

        print(res)
        return res




if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    #[2]

    # nums1 = [4, 9, 5]
    # nums2 = [9, 4, 9, 8, 4]
    # [9,4]

    # nums1 = [1, 2]
    # nums2 = [1, 1]

    solution = Solution()
    solution.intersection(nums1,nums2)