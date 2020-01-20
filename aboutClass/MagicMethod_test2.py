"""
- 定制一个计时器类

　　- start和stop方法代表启动和停止计时

　　- 假设计时器对象t1,定制t1对象直接执行和打印时的输出信息

　　- 当计时器未启动或已经停止计时，调用stop方法会给予温馨提示

　　- 两个计时器对象可以进行相加： t1 + t2
"""
import time

class Timer:
    def __init__(self):
        self._start = None
        self._stop = None
        self._delta = 0

    def start(self):
        if not self._start:
            self._start = time.time()
        else:
            print("已经开始了")

    def stop(self):
        if not self._stop and  self._start:
            self._stop = time.time()
            self.__calc()
        elif not self._start:
            print("未开始")
        else:
            print("已经终止")


    def __calc(self):
        self._delta += self._stop - self._start
        self._start = None
        self._stop = None

    def __repr__(self):
        return "计时：{:.2f}".format(self._delta)

    def getDelta(self):
        return self._delta

    def __add__(self, other):
        return self._delta + other.getDelta()

T1 = Timer()
T2 = Timer()
T1.start()
time.sleep(3)
T1.stop()
T1.start()
time.sleep(1)
T1.stop()
print( T1+T2 )
print(T1)

