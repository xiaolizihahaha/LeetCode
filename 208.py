class Trie(object):

    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False


    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self
        for w in word:
            if node.children[ord(w) - ord('a')] is None:
                node.children[ord(w) - ord('a')] = Trie()
            node = node.children[ord(w) - ord('a')]
        node.isEnd = True


    def searchStr(self, word):
        """
        :type word: str
        :rtype: node
        """
        node = self
        for w in word:
            if node.children[ord(w) - ord('a')] is None:
                return None
            node = node.children[ord(w) - ord('a')]
        return node




    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.searchStr(word)
        if node is not None and node.isEnd is True:
            return True
        return False



    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self.searchStr(prefix)
        if node is not None:
            return True
        return False





# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)