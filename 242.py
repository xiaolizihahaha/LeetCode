class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        sdic = dict()
        tdic = dict()

        for i in range(len(s)):
            if sdic.get(s[i]) is None:
                sdic[s[i]] = 0
            sdic[s[i]] += 1

            if tdic.get(t[i]) is None:
                tdic[t[i]] = 0
            tdic[t[i]] += 1

        for ch, val in sdic.items():
            if tdic.get(ch) != val:
                return False
        return True

if __name__ == '__main__':
    # s = "anagram"
    # t = "nagaram"

    s = "rat"
    t = "car"
    solution = Solution()
    result = solution.isAnagram(s,t)
    print(result)