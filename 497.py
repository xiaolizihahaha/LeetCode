import random
class Solution(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.r = list()
        for rect in rects:
            xmin = min(rect[0],rect[2])
            xmax = max(rect[0],rect[2])
            ymin = min(rect[1],rect[3])
            ymax = max(rect[1],rect[3])

            self.r.append([xmin,xmax,ymin,ymax])

    def pick(self):
        """
        :rtype: List[int]
        """
        id = random.choices(range(len(self.r)),[(i[1] - i[0] + 1)*(i[3] - i[2] + 1)for i in self.r])[0]
        x = random.choice(range(self.r[id][0],self.r[id][1]+1))
        y = random.choice(range(self.r[id][2],self.r[id][3]+1))

        print(x,y)
        return [x,y]



# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()

if __name__ == '__main__':
    rects = [[-2, -2, 1, 1], [2, 2, 4, 6]]
    solution = Solution(rects)
    solution.pick()