class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        if len(nums1) > len(nums2):
            return self.helper(nums2,nums1)
        else:
            return self.helper(nums1,nums2)



    def maxsame(self,nums1,index1,nums2,index2,len):
        if len == 0:
            return 0

        ret = 0
        temp = 0
        for i in range(len):
            if nums1[index1+i] == nums2[index2+i]:
                temp += 1
            else:
                ret = max(ret,temp)
                temp = 0

        ret = max(ret,temp)
        return ret

    def helper(self,shorter,longer):
        ret = 0

        for i in range(len(shorter)):
            temp = self.maxsame(shorter,len(shorter)-i-1,longer,0,i+1)
            ret = max(ret,temp)

        for i in range(len(longer)-len(shorter)):
            temp = self.maxsame(shorter,0,longer,1+i,len(shorter))
            ret = max(ret,temp)

        for i in range(len(shorter)):
            temp = self.maxsame(shorter,0,longer,len(longer)-len(shorter)+i+1,len(shorter)-i-1)
            ret = max(ret,temp)

        return ret



if __name__ == '__main__':
    nums1 = [1, 2, 3, 2, 1]
    nums2 = [3, 2, 1, 4, 7]

    # nums1 = [0, 0, 0, 0, 0]
    # nums2 = [0, 0, 0, 0, 0]
    solution = Solution()
    solution.findLength(nums1,nums2)