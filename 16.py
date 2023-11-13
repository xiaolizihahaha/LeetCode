class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = nums[0] + nums[1] + nums[len(nums)-1]
        cmp = abs((nums[0] + nums[1] + nums[len(nums)-1]) - target)
        nums.sort()
        # print(nums)
        for i in range(len(nums)-2):
            if i != 0:
                if nums[i-1] == nums[i]:
                    continue
            left = i + 1
            right = len(nums) - 1
            # print(i,left,right)
            while left != right:
                if nums[i] + nums[left] + nums[right] < target:
                    if abs((nums[i] + nums[left] + nums[right]) - target) < cmp:
                        result = nums[i] + nums[left] + nums[right]
                        cmp = abs((nums[i] + nums[left] + nums[right]) - target)
                    left += 1
                elif nums[i] + nums[left] + nums[right] > target:
                    if abs((nums[i] + nums[left] + nums[right]) - target) < cmp:
                        result = nums[i] + nums[left] + nums[right]
                        cmp = abs((nums[i] + nums[left] + nums[right]) - target)
                    right -= 1
                elif nums[i] + nums[left] + nums[right] == target:
                    if abs((nums[i] + nums[left] + nums[right]) - target) < cmp:
                        result = nums[i] + nums[left] + nums[right]
                        cmp = abs((nums[i] + nums[left] + nums[right]) - target)
                    break

        print(result)
        return result



if __name__ == '__main__':
    nums = [-1, 2, 1, -4]
    target = 1

    nums = [0, 1, 2]
    target = 3

    solution = Solution()
    solution.threeSumClosest(nums,target)