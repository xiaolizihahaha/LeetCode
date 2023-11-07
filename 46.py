class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        results = list()
        self.traceBack(nums,[],results,len(nums))

        print(results)
        return results
    def traceBack(self,nums,path,results,n):
        if len(nums) == 0 and len(path) == n:
            results.append(path[:])
            return

        for index,num in enumerate(nums):
            # print(nums)
            nums.pop(index)
            path.append(num)


            self.traceBack(nums,path,results,n)

            nums.insert(index,num)
            path.pop(-1)




if __name__ == '__main__':
    nums = [1, 2, 3]
    # nums = [0,1]
    # nums = [1]
    solution = Solution()
    solution.permute(nums)