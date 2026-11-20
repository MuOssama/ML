import math

class Statistics:
    def __init__(self, data):
        self._list = sorted(data)
        self.len = len(self._list)

    def median(self):
        index = int(self.len/2)
        if self.len % 2 != 0:
            return self._list[index]
        return (self._list[index]+self._list[index-1])/2


    def mean(self):
        sum = 0
        for item in self._list:
             sum += item
        return sum/self.len

    def variance(self):
        sum = 0
        mean = self.mean()
        for item in self._list:
           sum += (item-mean)**2
        return sum/self.len


    def deviation(self):
          return math.sqrt(self.variance())

    def Z(self, X):
        return (X-self.mean())/self.deviation()
    

    def standerdize(self):
        std_list = []
        for item in self._list:
           std_list.append(self.Z(item))

        return std_list

    def check_skewneess(self):
        sum = 0
        for item in self._list:
            sum += self.Z(item) ** 3
        return sum/self.len





