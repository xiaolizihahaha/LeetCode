class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        hash = dict()
        hash1 = dict()
        result1 = list()
        result = list()
        for num in nums:
            if hash.get(num) is None:
                hash[num] = 0
            hash[num] += 1

        # print(hash)

        for key,val in hash.items():
            if hash1.get(val) is None:
                result1.append(val)
                hash1[val] = []
            hash1[val].append(key)

        # print(hash1)
        #
        result1 = sorted(result1,reverse=True)
        # print(result1)

        i = 0
        while len(result) < k:
            result.extend(hash1.get(result1[i]))
            i += 1


        return result






        # for i in range(k):
        #     new = nums[hash.]
        #     result.append(new)
        #     i += 1


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    # 输出: [1, 2]
    #
    # nums = [1]
    # k = 1

    # nums = [3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6]
    # k = 10
    # 输出: [1]

    solution = Solution()
    result = solution.topKFrequent(nums,k)
    print(result)