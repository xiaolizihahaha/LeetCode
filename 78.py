class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = list()
        self.traceBack(nums,len(nums),[],results)

        print(results)
        return results

    def traceBack(self,nums,n,path,results):
        if len(path) <= n:
            results.append(path[:])
        if len(path) == n:
            return

        for index,num in enumerate(nums):
            path.append(num)
            self.traceBack(nums[index+1:],n,path,results)


            path.pop(-1)


if __name__ == '__main__':
    nums = [1, 2, 3]
    # nums = [0]

    solution = Solution()
    solution.subsets(nums)