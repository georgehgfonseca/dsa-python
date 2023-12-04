# Design a class that has three methods:
# 1. Inserting a value (no duplicates)
# 2. Removing a value
# 3, Get a random value that is already insert (with equal probability)
# Based on https://www.youtube.com/watch?v=46dZH7LDbf8&ab_channel=NeetCode

import random

class Holder:

    def __init__(self):
        self.data_index = dict()
        self.data = list()

    def insert(self, value):
        if value in self.data_index:
            return
        
        self.data.append(value)
        self.data_index[value] = len(self.data) - 1

    def remove(self, value):
        if value not in self.data_index:
            return
        
        index = self.data_index[value]
        self.data[index], self.data[-1] = self.data[-1], self.data[index]

        # fix dictionary
        self.data_index[self.data[index]] = index
        self.data_index.pop(value)

        self.data.pop()

    def random(self):
        if self.data:
            return random.choice(self.data)

# 
# data      : [5, 6]
# data_index: {5:0, 6:1}
# index     : 1 
h = Holder()
h.insert(5)
h.insert(4)
h.insert(4)
h.insert(6)
h.remove(2)
h.remove(4)
h.random()
print(h.data, h.data_index)