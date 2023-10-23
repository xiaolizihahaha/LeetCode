class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        nums3 = []
        i = 0
        j = 0

        nums1length = len(nums1)
        nums2length = len(nums2)

        while i < nums1length and j <nums2length :
            if nums1[i] <= nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1
        while i < nums1length:
            nums3.append(nums1[i])
            i += 1

        while j < nums2length:
            nums3.append(nums2[j])
            j += 1



        num3length = nums1length + nums2length

        if num3length % 2 == 0:
            return (nums3[int(num3length/2)-1]+nums3[int(num3length/2)]) * 1.0 / 2

        else:
            return nums3[int(num3length/2)]





if __name__ == '__main__':

    # 输入：nums1 = [1, 3], nums2 = [2]
    # 输出：2.00000
    # 解释：合并数组 = [1, 2, 3] ，中位数

    # 输入：nums1 = [1, 2], nums2 = [3, 4]
    # 输出：2.50000
    # 解释：合并数组 = [1, 2, 3, 4] ，中位数(2 + 3) / 2 = 2.5
    #

    # nums1 = [1,2]
    # nums2 = [3,4]

    #
    # nums1 = [1,3]
    # nums2 = [2]


    # nums1 = [1,3]
    # nums2 = [2,7]


    solution = Solution()
    result = solution.findMedianSortedArrays(nums1=nums1,nums2=nums2)
    print(result)