class Solution(object):
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        """
        :type nums: List[int]
        :type firstLen: int
        :type secondLen: int
        :rtype: int
        """
        if firstLen + secondLen == len(nums):
            return sum(nums)



        if firstLen < secondLen:
            temp = firstLen
            firstLen = secondLen
            secondLen = temp


        left1 = 0
        right1 = left1 + firstLen - 1
        left2 = right1 + 1
        right2 = left2 + secondLen - 1

        maxsum = 0
        sum1 = 0
        sum2 = 0
        sum12 = sum1 + sum2
        # print(sum12)

        while right1 < len(nums):
            if left1 == 0:
                sum1 = sum(nums[left1:right1+1])
            else:
                sum1 += nums[right1]
                sum1 -= nums[left1-1]

            if len(nums) - right1 -1 >= secondLen:
                left2 = right1 + 1
                right2 = left2 + secondLen - 1

                while right2 < len(nums):
                    if left2 == right1 + 1:
                        sum2 = sum(nums[left2:right2+1])
                    else:
                        sum2 += nums[right2]
                        sum2 -= nums[left2-1]

                    # sum2 = sum(nums[left2:right2+1])
                    sum12 = sum1 + sum2
                    maxsum = max(maxsum,sum12)
                    left2 += 1
                    right2 += 1

            if left1 >= 2:
                left2 = 0
                right2 = left2 + secondLen - 1

                while right2 < left1:

                    if left2 == 0:
                        sum2 = sum(nums[left2:right2+1])
                    else:
                        sum2 += nums[right2]
                        sum2 -= nums[left2-1]

                    # sum2 = sum(nums[left2:right2+1])
                    sum12 = sum1 + sum2
                    maxsum = max(maxsum,sum12)
                    left2 += 1
                    right2 += 1


            left1 += 1
            right1 += 1

        print(maxsum)
        return maxsum






if __name__ == '__main__':
    nums = [0, 6, 5, 2, 2, 5, 1, 9, 4]
    firstLen = 1
    secondLen = 2

    # nums = [3, 8, 1, 3, 2, 1, 8, 9, 0]
    # firstLen = 3
    # secondLen = 2
    #
    # nums = [2, 1, 5, 6, 0, 9, 5, 0, 3, 8]
    # firstLen = 4
    # secondLen = 3
    solution = Solution()
    solution.maxSumTwoNoOverlap(nums,firstLen,secondLen)