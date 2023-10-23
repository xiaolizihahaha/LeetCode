class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        nums = list(set(nums))
        nums = sorted(nums)

        # print(nums)

        maxlen = 0
        templen = 1
        i = 0
        while i < len(nums) :
            if i == len(nums) -1:
                if maxlen < templen:
                    maxlen = templen
                    templen = 1
                i += 1
            else :
                if nums[i+1] == nums[i] + 1:

                    # print("continue",nums[i],"to",nums[i+1])

                    templen += 1
                    i += 1
                    # print(templen)

                else :
                    # print("stop",nums[i],"to",nums[i+1])
                    if maxlen < templen:
                        maxlen = templen
                    templen = 1
                    # print(templen)
                    i += 1


        return maxlen

if __name__ == '__main__':

    # nums = [100, 4, 200, 1, 3, 2]
    # 输出：4

    # nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    # 输出：9

    nums = [9, 1, -3, 2, 4, 8, 3, -1, 6, -2, -4, 7]
    solution = Solution()
    result = solution.longestConsecutive(nums)
    print(result)