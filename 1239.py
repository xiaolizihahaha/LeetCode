import copy


class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        arr1 = list()
        results = list()
        results.append('')
        for a in arr:
            d = dict()
            sig = True
            for i in a:
                if d.get(i) is None:
                    d[i] = 1
                else:
                    sig = False
                    break
            if sig is True:
                arr1.append(a)

        if len(arr1) == 0:
            print(0)
            return 0
        if len(arr1) == 1:
            print(len(arr1[0]))
            return len(arr1[0])


        print(arr1)
        d1 = dict()
        self.dfs(arr1,'',results,d1)
        print(results)
        print(len(results[0]))
        return len(results[0])

    def dfs(self,arr,path,results,d):
        if len(arr) >= 0:
            # print(path)
            if len(path) > len(results[0]):
                results[0] = path
        if len(arr) == 0:
            return

        for index,a in enumerate(arr):
            if a in arr[:index]:
                continue

            d1 = copy.deepcopy(d)
            sig = True
            for i in a:
                if d1.get(i) is None:
                    d1[i] = 1
                    continue
                else:
                    sig = False
                    break
            if sig is True:
                self.dfs(arr[index+1:],path + a,results,d1)




if __name__ == '__main__':
    # arr = ["un", "iq", "ue"]
    arr = ["cha", "r", "act", "ers"]
    arr = ["abcdefghijklmnopqrstuvwxyz"]
    arr = ['abd','ceds','wera','wer']
    arr = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]

    solution = Solution()
    solution.maxLength(arr)