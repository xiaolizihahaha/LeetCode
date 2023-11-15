class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        p = 0
        q = len(s) - 1

        while p <= (len(s) - 1) // 2:
            temp = s[p]
            s[p] = s[q]
            s[q] = temp

            p += 1
            q -= 1