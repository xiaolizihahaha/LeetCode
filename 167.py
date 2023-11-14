class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = list()
        p = 0
        q = len(numbers) - 1

        while p != q:
            if numbers[p] + numbers[q] < target:
                p += 1
            elif numbers[p] + numbers[q] > target:
                q -= 1
            elif numbers[p] + numbers[q] == target:
                result.append(p+1)
                result.append(q+1)
                print(result)
                return result


if __name__ == '__main__':
    # numbers = [2, 7, 11, 15]
    # target = 9

    # numbers = [2, 3, 4]
    # target = 6
    #
    numbers = [-1, 0]
    target = -1
    solution = Solution()
    solution.twoSum(numbers,target)