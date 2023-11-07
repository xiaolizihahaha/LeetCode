class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        re = []

        self.dfs(nums,[],results,len(nums))
        for result in results:
            result.sort()
            if result not in re:
                re.append(result)
        print(re)
        return re

    def dfs(self,nums,path,results,n):
        if len(path) <= n:
            results.append(path[:])
        if len(path) == n:
            return

        for index,num in enumerate(nums):
            if num in nums[:index]:
                continue
            path.append(num)
            self.dfs(nums[index+1:],path,results,n)

            path.pop(-1)

if __name__ == '__main__':
    nums = [1, 2, 2]
    # nums = [0]
    solution = Solution()
    solution.subsetsWithDup(nums)
