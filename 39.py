import copy


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = list()
        self.traceBack(candidates,target,[],result)
        return result


    def traceBack(self,candidates,target,path,result):
        if sum(path) > target:
            return
        if sum(path) == target:
            p1 = sorted(path)
            if p1 not in result:
                result.append(copy.deepcopy(p1))
            return

        for candidate in candidates:
            path.append(candidate)
            self.traceBack(candidates,target,path,result)
            path.pop(-1)

if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    c = [2,3,6,7]
    print(candidates == c)
    target = 7
    solution = Solution()
    solution.combinationSum(candidates,target)