class LRUCache(object):
    '''
    缓存淘汰算法 LRU（Least recently used，最近最少使用）算法

    原则：
        新数据插入到链表头部；
        每当缓存命中（即缓存数据被访问），则将数据移到链表头部；
        当链表满的时候，将链表尾部的数据丢弃。
    '''

    #只定义了dic

    # def __init__(self, capacity):
    #     """
    #     :type capacity: int
    #     """
    #     self.capacity1 = capacity
    #     self.cache = {}
    #
    #
    # def get(self, key):
    #     """
    #     :type key: int
    #     :rtype: int
    #     """
    #     if self.cache.get(key) is None:
    #         return -1
    #     else:
    #         value = self.cache[key]
    #         self.cache.pop(key)
    #         self.cache[key] = value
    #         return value
    #
    #
    #
    # def put(self, key, value):
    #     """
    #     :type key: int
    #     :type value: int
    #     :rtype: None
    #     """
    #     if self.cache.get(key) is not None:
    #         self.cache.pop(key)
    #         self.cache[key] = value
    #
    #     else:
    #         if len(self.cache) < self.capacity1:
    #             self.cache[key] = value
    #         else:
    #             key1 = ''
    #             value1 = ''
    #             for key2, value2 in self.cache.items():
    #                 key1 = key2
    #                 value1 = value2
    #                 break
    #             self.cache.pop(key1)
    #             self.cache[key] = value


    #定义了dic和list，list只放key
    '''
        其中dic存放key-value的映射，pop时为了节省时间不进行删除操作，只删除list中的元素，且为了节省时间，列表头部（index = 0）处存放最新访问过的元素的key，尾部被淘汰。
    '''
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.line = list()
        self.cache = dict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.line:
            return -1
        else:
            value = self.cache.get(key)
            self.line.remove(key)
            self.line.insert(0,key)

            return value


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.line:
            self.cache[key] = value
            self.line.remove(key)
            self.line.insert(0,key)
        else:
            if len(self.line) < self.capacity:
                self.line.insert(0,key)
                self.cache[key] = value
            else:
                self.line.pop(-1)
                self.line.insert(0,key)
                self.cache[key] = value









# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':

    # d = {'1':1,"2":2}
    # d['1'] = 2
    # print(d)
    #
    # l = ['1','2','3','4']
    # l.append('5')
    #
    # l.remove('2')
    # l.insert(len(l),'2')
    # print(l)



    capacity = 2
    obj = LRUCache(capacity)

    obj.put('1',1)
    # print(obj.cache)
    obj.put('2',2)
    # print(obj.cache)

    param_1 = obj.get('1')
    # print(obj.cache)
    print(param_1)

    obj.put('3',3)
    # print(obj.cache)

    param_2 = obj.get('2')
    # print(obj.cache)
    print(param_2)

    obj.put('4',4)
    # print(obj.cache)

    param_2 = obj.get('1')
    # print(obj.cache)
    print(param_2)

    param_2 = obj.get('3')
    # print(obj.cache)
    print(param_2)

    param_2 = obj.get('4')
    # print(obj.cache)
    print(param_2)








'''
示例：

输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]

解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4
'''