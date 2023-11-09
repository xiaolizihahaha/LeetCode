class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = list()
        result.append(0)
        sum = 0
        time = 0
        self.dfs(nums,target,sum,time,len(nums),result)
        # print(results.count(1))
        # print(results[0])
        count = result[0]
        print(count)
        return count

    def dfs(self,nums,target,sum,time,k,result):
        if time == k:
            if sum == target:
                result[0] += 1
            return

        self.dfs(nums,target,sum+nums[time],time+1,k,result)
        self.dfs(nums,target,sum-nums[time],time+1,k,result)


if __name__ == '__main__':
    # nums = [1, 1, 1, 1, 1]
    # target = 3

    # nums = [1]
    # target = 1

    nums = [42, 16, 31, 11, 36, 19, 9, 3, 25, 0, 27, 29, 35, 29, 45, 15, 35, 42, 35, 23]
    target = 39
    solution = Solution()
    solution.findTargetSumWays(nums,target)