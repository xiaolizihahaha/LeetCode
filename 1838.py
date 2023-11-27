class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sortnums = sorted(nums,reverse=True)
        print(sortnums)

        numd = dict()
        r = 0
        l = 0
        maxres = 0

        while r < len(sortnums):
            if len(numd) == 0:
                if sortnums[r] not in numd:
                    numd[sortnums[r]] = 0
            else:
                if sortnums[r] not in numd:
                    numd[sortnums[r]] = 0
                for key in numd.keys():
                    numd[key] += key - sortnums[r]
            r += 1

            while l < r and numd[sortnums[l]] > k:
                maxres = max(maxres,r - l - 1)
                l += 1
                if sortnums[l-1] != sortnums[l]:
                    temp = sortnums[l-1]
                    numd.pop(temp)



        if numd[sortnums[l]] <= k :
            maxres = max(maxres,r - l)
        else:
            maxres = max(maxres,r - l - 1)



        print(maxres)
        return maxres





if __name__ == '__main__':
    nums = [1, 2, 4]
    k = 5

    nums = [3, 9, 6]
    k = 2

    nums = [1, 4, 8, 13]
    k = 5

    nums = [1,1,2,6,8,8,9,9,9,10]
    k = 3

    nums = [9930,9923,9983,9997,9934,9952,9945,9914,9985,9982,9970,9932,9985,9902,9975,9990,9922,9990,9994,9937,9996,9964,9943,9963,9911,9925,9935,9945,9933,9916,9930,9938,10000,9916,9911,9959,9957,9907,9913,9916,9993,9930,9975,9924,9988,9923,9910,9925,9977,9981,9927,9930,9927,9925,9923,9904,9928,9928,9986,9903,9985,9954,9938,9911,9952,9974,9926,9920,9972,9983,9973,9917,9995,9973,9977,9947,9936,9975,9954,9932,9964,9972,9935,9946,9966]
    k = 3056

    nums = [1,2,3,4,5,7,7,7,8,9,11,13]
    k = 5

    nums = [9940,9995,9944,9937,9941,9952,9907,9952,9987,9964,9940,9914,9941,9933,9912,9934,9980,9907,9980,9944,9910,9997]
    k = 7925

    nums = [1,1,1,3,3,3]
    k = 7

    solution = Solution()
    solution.maxFrequency(nums, k)