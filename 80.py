class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p = 0
        q = 0
        cur = nums[0]
        count = 0
        while q < len(nums):
            cur = nums[q]
            count = 0
            while nums[q] == cur:
                q += 1
                count += 1
                if q >= len(nums):
                    break

            #此时 q指向新的cur count是刚刚cur的count个数
            shouldadd = min(count,2)
            for i in range(shouldadd):
                nums[p] = cur
                p += 1

        k = p
        print(k,nums)
        return k

if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    solution = Solution()
    solution.removeDuplicates(nums)

