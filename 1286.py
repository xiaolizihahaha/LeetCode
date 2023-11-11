class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        self.results = list()
        self.dfs(characters,combinationLength,'',self.results)
        print(self.results)
        self.cur = 0




    def next(self):
        """
        :rtype: str
        """
        if self.hasNext():
            temp = self.results[self.cur]
            self.cur += 1
            print(temp)
            return temp


    def hasNext(self):
        """
        :rtype: bool
        """
        if self.cur < len(self.results):
            print('true')
            return True
        else:
            print('false')
            return False

    def dfs(self,characters, combinationLength,path,results):
        if len(path) == combinationLength:
            results.append(path)
            return
        for index,c in enumerate(characters):
            self.dfs(characters[index+1:],combinationLength,path + c, results)

if __name__ == '__main__':
    characters = 'abc'
    combinationLength = 2
    # Your CombinationIterator object will be instantiated and called as such:
    obj = CombinationIterator(characters, combinationLength)
    param_1 = obj.next()
    param_1 = obj.next()
    param_1 = obj.next()
    param_2 = obj.hasNext()