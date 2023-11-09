class Solution(object):
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        results = list()
        results.append(0)

        nums = list()
        for i in range(n):
            nums.append(i+1)

        print(nums)

        self.dfs(nums,1,[],results,n)
        print(results[0])

        return results[0]

    def dfs(self,nums,time,path,results,n):
        if time == n+1:
            # print(path)
            results[0] += 1
            return

        for index,num in enumerate(nums):
            if num % time == 0 or time % num == 0:
                nums.pop(index)
                path.append(num)
                self.dfs(nums,time+1,path,results,n)
                path.pop(-1)
                nums.insert(index,num)


if __name__ == '__main__':
    n = 3
    solution = Solution()
    solution.countArrangement(n)