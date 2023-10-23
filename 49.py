class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        result = []
        seperates = []

        for str in strs:
            seperate1 = []
            for i in range(len(str)):
                seperate1.append(str[i])
            seperate1 = sorted(seperate1)
            if seperates.count(seperate1) == 0:
                seperates.append(seperate1)
                result1 = []
                result1.append(str)
                result.append(result1)
            else:
                index = seperates.index(seperate1)
                result[index].append(str)

            # print(seperate1)

        return result

if __name__ == '__main__':
    # strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # strs = [""]
    strs = ["a"]

    solution = Solution()
    result = solution.groupAnagrams(strs)
    print(result)