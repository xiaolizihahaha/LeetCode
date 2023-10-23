import copy


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        # 太慢了

        totallength = len(words) * len(words[0])
        slength = len(s)

        s1 = copy.deepcopy(s)
        s1 += ' ' * (totallength)

        result = []

        for i in range(slength):
            subList = []
            substr = s1[i:i+totallength]
            for j in range(len(words)):
                subList.append(substr[j * len(words[0]):(j+1) * len(words[0])])

            if sorted(subList) == sorted(words):
                result.append(i)


        # 另一种 太复杂了 未完
        # s1 = copy.deepcopy(s)
        # s1 += ' ' * (len(words[0]) - 1)
        # matrix = []
        # result = []
        # slength = len(s)
        #
        # for j in range(len(words)):
        #     submarix = []
        #     for i in range(slength):
        #         if s1[i:i+len(words[0])] == words[j]:
        #             submarix.append(1)
        #         else:
        #             submarix.append(0)
        #     matrix.append(submarix)
        #
        # print(matrix)





        return result





if __name__ == '__main__':
    # s = "barfoothefoobarman"
    # words = ["foo", "bar"]

    # s = "wordgoodgoodgoodbestword"
    # words = ["word", "good", "best", "word"]
    #
    s = "barfoofoobarthefoobarman"
    words = ["bar", "foo", "the"]
    #
    # s = "wordgoodgoodgoodbestword"
    # words = ["word", "good", "best", "good"]

    # s = "ababaab"
    # words = ["ab", "ba", "ba"]


    solution = Solution()
    result = solution.findSubstring(s,words)
    print(result)