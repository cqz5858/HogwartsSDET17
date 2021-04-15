import logging
import threading
from time import sleep, ctime

logging.basicConfig(level=logging.INFO)

loops = [2, 4]

class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        self.func(*self.args)


def loop(nloop, nsec):
    logging.info("start loop " + str(nloop) + " at " + ctime())
    sleep(nsec)
    logging.info("end loop " + str(nloop) + " at " + ctime())

def main():
    logging.info("start all at " + ctime())
    # 声明一个空列表threads
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        # 每生成一个线程追加到threads
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    logging.info("end all at " + ctime())


if __name__ == '__main__':
    main()
# 多个线程可以访问同一个数据，但一定会产生错误
# 原语
# 锁 数据互置访问  True False
# 信号量 0 1 2 3
