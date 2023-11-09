class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = list()

        self.dfs(nums,[],results,len(nums))
        print(results)
        return results

    def dfs(self,nums,path,results,k):
        if len(path) >= 2:
            results.append(path[:])
        if len(path) == k:
            return

        for index,num in enumerate(nums):
            if num in nums[:index]:
                continue
            if len(path) == 0 or num >= path[-1]:
                path.append(num)
                self.dfs(nums[index+1:],path,results,k)
                path.pop(-1)


if __name__ == '__main__':
    nums = [4, 6, 7, 7]
    nums = [4, 4, 3, 2, 1]
    solution = Solution()
    solution.findSubsequences(nums)
