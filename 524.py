class Solution(object):
    def findLongestWord(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: str
        """
        dictionary.sort(key=lambda x:(-len(x),x))

        print(dictionary)

        for d in dictionary:
            i = 0
            j = 0
            while i != len(s) and j != len(d):
                if s[i] == d[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
                if j == len(d):
                    print(d)
                    return d
        print('')
        return ''



if __name__ == '__main__':
    # s = "abpcplea"
    # dictionary = ["ale", "apple", "monkey", "plea"]
    # 输出："apple"

    s = "abpcplea"
    dictionary = ["a", "b", "c"]
    # 输出："a"

    solution = Solution()
    solution.findLongestWord(s,dictionary)