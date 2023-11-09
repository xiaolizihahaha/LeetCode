class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        total = sum(nums)
        if total % k != 0:
            print('bb')
            return False

        nums.sort(reverse=True)
        a = total // k
        avoid = list()
        for index,num in enumerate(nums):
            if num > a:
                print('aa')
                return False
            if num == a:
                avoid.append(index)

        avoid.reverse()
        for i in avoid:
            nums.pop(i)

        k = k - len(avoid)


        if nums.count(a-1) > nums.count(1):
            print('ccc')
            return False

        avoid2 = list()
        avoid3 = list()
        for index,num in enumerate(nums):
            if num == a-1:
                avoid2.append(index)
            if num == 1:
                avoid3.append(index)


        avoid4 = avoid2[:] + avoid3[:len(avoid2)]
        avoid4.reverse()
        # print(len(avoid2))
        for i in avoid4:
            nums.pop(i)


        k = k - len(avoid2)

        print(nums)
        print(k)
        print(a)


        result = self.dfs(nums,k,k * [0],0,a)
        print(result)
        return result
    def dfs(self,nums,k,paths,index,a):
        if index == len(nums) and paths.count(a) == len(paths):
            return True

        for i in range(k):
            if nums[index] <= a - paths[i]:
                paths[i] += nums[index]
                if self.dfs(nums,k,paths,index+1,a) is True:
                    return True
                paths[i] -= nums[index]
        return False


if __name__ == '__main__':
    # nums = [4, 3, 2, 3, 5, 2, 1]
    # k = 4
    #
    # nums = [1, 2, 3, 4]
    # k = 3

    # nums = [3,9,4,5,8,8,7,9,3,6,2,10,10,4,10,2]
    # k = 10
    #
    nums = [1,1,1,1,2,2,2,2]
    k = 2

    solution = Solution()
    solution.canPartitionKSubsets(nums,k)
