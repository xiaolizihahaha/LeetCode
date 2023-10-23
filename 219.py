class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        numdic = dict()
        disdic = dict()
        for i in range(len(nums)):
            if numdic.get(nums[i]) is None:
                numdic[nums[i]] = []
                numdic[nums[i]].append(i)
                disdic[nums[i]] = []
                disdic[nums[i]].append(0)
            else:
                numdic[nums[i]].append(i)
                newNum = numdic[nums[i]][-1] - numdic[nums[i]][-2]
                disdic[nums[i]].append(newNum)


        # print("111",disdic)

        mindistance = -1
        for dis, val in disdic.items():
            print(dis,val)
            if len(val) > 1:
                mins = min(val[1:])
                if mindistance < 0 or mins < mindistance:
                    mindistance = mins


        if mindistance <= k and mindistance != -1:
            return True
        else:
            return False


if __name__ == '__main__':
    # 示例1：
    #
    # nums = [1, 2, 3, 1]
    # k = 3
    # 输出：true
    # 示例2：
    #
    # nums = [1, 0, 1, 1]
    # k = 1
    # 输出：true
    # 示例3：
    #
    # nums = [1, 2, 3, 1, 2, 3]
    # k = 2

    nums = [1]
    k = 2
    # 输出：false
    solution = Solution()
    result = solution.containsNearbyDuplicate(nums, k)
    print(result)
