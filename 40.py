import copy


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        result = list()
        self.traceBack(candidates,target,[],result)
        re = list()
        for r in result:
            r.sort()
            if r not in re:
                re.append(r)
        print(re)
        return re

    def traceBack(self,candidates, target,path,result):
        if sum(path) == target:
            result.append(path[:])
            return
        if sum(path) > target:
            return
        if len(candidates) <= 0:
            return

        for index,candidate in enumerate(candidates):
            if candidate in candidates[:index]:
                continue
            path.append(candidate)

            self.traceBack(candidates[index+1:],target,path,result)

            path.pop(-1)



if __name__ == '__main__':
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8


    # candidates = [2, 5, 2, 1, 2]
    # target = 5
    solution = Solution()
    solution.combinationSum2(candidates,target)