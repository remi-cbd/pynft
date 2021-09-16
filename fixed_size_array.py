#!/usr/bin/env python3

class fixedSizeArray(object):
    def __init__(self, arraySize):
        self.arraySize = arraySize
        self.array = [None] * self.arraySize

    def __repr__(self):
        return str(self.array)

    def __get__(self, instance, owner):
        return self.array

    def append(self, index=None, value=None):
        print("Append Operation cannot be performed on fixed size array")
        return

    def insert(self, index=None, value=None):
        if not index and index - 1 not in xrange(self.arraySize):
            print("invalid Index or Array Size Exceeded")
            return
        try:
            self.array[index] = value
        except:
            print("This is Fixed Size Array: Please Use the available Indices")