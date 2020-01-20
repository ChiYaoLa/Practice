class MyRange:
    def __init__(self,end):
        self._start = 0
        self._end = end
    def __iter__(self):
        return self

    def __next__(self):
        if self._start < self._end:
            ret = self._start
            self._start += 1
            return ret
        else:
            raise StopIteration

R = MyRange(5)
# print(next(R))
# for i in R:
#     print(i)
for i in iter(R):
    print(next(i))