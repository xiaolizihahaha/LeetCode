class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        # print(nums)
        if len(nums) < 4:
            return []
        results = list()

        for i in range(0,len(nums)-3):
            if i != 0:
                if nums[i] == nums[i-1]:
                    continue
            for j in range(i+1,len(nums)-2):
                if j != i+1:
                    if nums[j] == nums[j-1]:
                        continue
                start = j+1
                end = len(nums)-1
                # print(i,j,start,end)
                while start != end:
                    if nums[i] + nums[j] + nums[start] + nums[end] == target:
                        results.append([nums[i],nums[j],nums[start],nums[end]])
                        start += 1
                    elif nums[i] + nums[j] + nums[start] + nums[end] < target:
                        start += 1
                    elif nums[i] + nums[j] + nums[start] + nums[end] > target:
                        end -= 1
        re = list()
        for r in results:
            if r not in re:
                re.append(r)
        print(re)
        return re


if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    target = 0

    nums = [2, 2, 2, 2, 2]
    target = 8
    solution = Solution()
    solution.fourSum(nums,target)
