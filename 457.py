class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        for i in range(len(nums)):
            start = i
            cur = start
            sig = 'up'
            route = []

            if nums[start] > 0:
                sig = 'up'
            else:
                sig = 'down'

            if sig == 'up':

                pre = cur
                while nums[cur] > 0:
                    route.append(cur)
                    pre = cur
                    cur = cur + nums[cur]
                    if cur >= len(nums):
                        cur = cur % len(nums)
                    if cur in route and pre != cur:
                        print(1)
                        return True
                    if pre == cur:
                        break

            elif sig == 'down':

                pre = cur
                while nums[cur] < 0:
                    route.append(cur)
                    pre = cur
                    cur = cur + nums[cur]
                    if cur < 0:
                        cur = cur % len(nums)
                    if cur in route and pre != cur:
                        print(1)
                        return True
                    if pre == cur:
                        break
        print(-1)
        return False


if __name__ == '__main__':
    # nums = [2, -1, 1, 2, 2]
    #
    # nums = [-1, 2]
    nums = [-2, 1, -1, -2, -2]
    nums = [1,1,2]
    nums = [-2,-17,-1,-2,-2]
    solution = Solution()
    solution.circularArrayLoop(nums)



