#coding=utf-8
import  _thread
from time import sleep, ctime

loops = [4, 2]


def loop(nloop, nsec, lock):
    print('start loop', nloop, 'at:%r' % ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:%r' % ctime())
    # 解锁
    lock.release()


def main():
    print('start:%r' % ctime())
    locks =[]
    # 以loops 数组创建列表，并赋值给nloops
    nloops = range(len(loops))
    for i in nloops:
        lock = _thread.allocate_lock()
        # 锁定
        lock.acquire()
        # 追加到locks[]数组中
        locks.append(lock)
    # 执行多线程
    for i in nloops:
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))
    for i in nloops:
        while locks[i].locked():
            pass
    print('all end:%r' % ctime())

if __name__ == '__main__':
    main()
