class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        res = list()
        maxnum = max(nums2)
        for num in nums1:
            if num == maxnum:
                res.append(-1)
            else:
                if nums2.index(num) == len(nums2) - 1:
                    res.append(-1)
                else:
                    index = nums2.index(num)
                    i = index
                    while i < len(nums2):
                        if nums2[i] <= num:
                            i += 1
                        else:
                            break
                    if i != len(nums2):
                        res.append(nums2[i])
                    else:
                        res.append(-1)

        print(res)
        return res




if __name__ == '__main__':
    # nums1 = [4, 1, 2]
    # nums2 = [1, 3, 4, 2]

    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    solution = Solution()
    solution.nextGreaterElement(nums1,nums2)