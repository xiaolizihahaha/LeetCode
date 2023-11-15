class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

        p = 0
        q = 0
        cur = chars[0]
        count = 0

        while p < len(chars) and q < len(chars):
            cur = chars[q]
            count = 0
            while q < len(chars) and chars[q] == cur:
                count += 1
                q += 1
            # if q >= len(chars):
            #     break

            if count == 1:
                chars[p] = cur
                p += 1
            else:
                chars[p] = cur
                newcount = str(count)
                for i in range(len(newcount)):
                    chars[p+i+1] = newcount[i]

                p += 1
                p += len(newcount)

        print(p,q,chars)
        return p



if __name__ == '__main__':
    chars = ["a", "a", "b", "b", "c", "c", "c"]
    # 返回6，输入数组的前6个字符应该是：["a", "2", "b", "2", "c", "3"]

    # chars = ["a"]
    # 返回1 ，输入数组的前1个字符应该是：["a"]

    # chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    # 返回4 ，输入数组的前4个字符应该是：["a", "b", "1", "2"]

    # chars = ["a", "a", "a", "b", "b", "a", "a"]

    solution = Solution()
    solution.compress(chars)