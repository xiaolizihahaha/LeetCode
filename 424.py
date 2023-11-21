class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        right = 0

        d = dict()
        d[s[left]] = 1
        # print(d)

        res = -1

        while left < len(s):
            remain = right - left + 1 - max(d.values())
            if remain <= k:
                right += 1
                if right >= len(s):
                    length = right - left
                    if length > res:
                        res = length
                    break
                if s[right] not in d:
                    d[s[right]] = 1
                else:
                    d[s[right]] += 1
            else:
                length = right - left
                if length > res:
                    res = length

                d[s[left]] -= 1
                left += 1

        print(res)
        return res






if __name__ == '__main__':
    s = "ABAB"
    k = 2

    s = "AABABBA"
    k = 1

    s = 'ABAA'
    k = 0
    solution = Solution()
    solution.characterReplacement(s,k)
    #
    # d = {'a':2,'b':3,'c':4}
    # print(max(d.values()))