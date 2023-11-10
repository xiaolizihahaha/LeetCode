class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """

        results = list()

        self.dfs(tiles,'',results,1,len(tiles))
        # print(results)
        print(len(results))
        return len(results)


    def dfs(self,tiles,path,results,time,k):
        if time <= k+1 and len(path) > 0:
            results.append(path[:])
        if time == k+1:
            return
        for index,tile in enumerate(tiles):
            if tile in tiles[:index]:
                continue
            else:
                temp = tiles[:index]
                temp += tiles[index+1:]
                self.dfs(temp,path + tile,results,time+1,k)


if __name__ == '__main__':

    tiles = 'AAB'
    # tiles = "AAABBC"
    tiles = 'V'
    solution = Solution()
    solution.numTilePossibilities(tiles)