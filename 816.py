class Solution(object):
    def ambiguousCoordinates(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        results = list()
        for i in range(2,len(s)-1):
            temp1 = s[1:i]
            temp = ','
            temp2 = s[i:len(s)-1]
            if temp1.count('0') >= 2 and temp1.count('0') == len(temp1) or temp2.count('0') >= 2 and temp2.count('0') == len(temp2) or temp1.count('0') >= 2 and temp1.startswith('0') and temp1.endswith('0') or temp2.count('0') >= 2 and temp2.startswith('0') and temp2.endswith('0'):
                continue

            temp1s = list()
            temp2s = list()

            self.dfs(temp1,temp1s)
            self.dfs(temp2,temp2s)

            print(temp1,temp2)
            print(temp1s,temp2s)

            for t1 in temp1s:
                for t2 in temp2s:
                    results.append("(" + t1 + ", " + t2 + ")")


            #此时i下标即 , 位置（前插）


        print(results)
        return results

    def dfs(self,temp,results):
        if len(temp) == 1:
            results.append(temp)
            return
        elif temp.startswith('0'):
            t = '0.' + temp[1:]
            results.append(t)
            return
        elif temp.endswith('0'):
            results.append(temp)
            return
        else:
            for i in range(1,len(temp)):
                results.append(temp[:i] + '.' + temp[i:])
            results.append(temp)




if __name__ == '__main__':
    s = '(123)'
    # s = '(00011)'
    # s = '(0123)'
    # s = '(100)'
    s = "(0010)"
    solution = Solution()
    solution.ambiguousCoordinates(s)