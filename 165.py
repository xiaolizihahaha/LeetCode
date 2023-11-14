class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        p = 0
        q = 0

        temp1 = ''
        temp2 = ''

        while p < len(version1) and q < len(version2):
            temp1 = ''
            temp2 = ''
            while p < len(version1) and version1[p] != '.' :
                temp1 += version1[p]
                p += 1
            if p < len(version1) and version1[p] == '.':
                p += 1
            while q <len(version2) and version2[q] !='.' :
                temp2 += version2[q]
                q += 1
            if q < len(version2) and version2[q] == '.':
                q += 1
            # print(temp1,temp2)
            if int(temp1) > int(temp2):
                print(1)
                return 1
            elif int(temp1) < int(temp2):
                print(-1)
                return -1


        if p == len(version1) and q == len(version2):
            if int(temp1) == int(temp2):
                print(0)
                return 0
            elif int(temp1) > int(temp2):
                print(1)
                return 1
            elif int(temp1) < int(temp2):
                print(-1)
                return -1
        print(p,q)

        temp1 = ''
        temp2 = ''


        while p < len(version1):
            temp1 = ''
            while p < len(version1) and version1[p] != '.':
                temp1 += version1[p]
                p += 1
            p += 1
            if int(temp1) > 0:
                print(1)
                return 1

        while q < len(version2):
            temp2 = ''
            while q < len(version2) and version2[q] != '.':
                temp2 += version2[q]
                q += 1
            q += 1
            if int(temp2) > 0:
                print(-1)
                return -1
        print(0)
        return 0





if __name__ == '__main__':
    version1 = "1.01"
    version2 = "1.001"

    version1 = "1.0"
    version2 = "1.0.0"

    version1 = "1.0"
    version2 = "1.0.4"


    solution = Solution()
    solution.compareVersion(version1,version2)