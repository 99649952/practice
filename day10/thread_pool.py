#!/usr/bin/env python
#coding:utf-8
import Queue
import threading
import time

class WorkManager(object):
    def __init__(self, work_num=1000,thread_num=2):
        self.work_queue = Queue.Queue() #创建队列
        self.threads = [] #创建空列表,用于存取Work类实例化后的对象
        self.__init_work_queue(work_num) #初始化线程
        self.__init_thread_pool(thread_num) #初始化工作队列

    def __init_thread_pool(self,thread_num): #启用一定个数的线程
        for i in range(thread_num):
            self.threads.append(Work(self.work_queue))  #为线程池启用相应个数的线程，并且传入队列

    def __init_work_queue(self, jobs_num): #工作个数
        for i in range(jobs_num):  #执行任务的个数
            self.add_job(do_job, i)#要执行的任务

    """ 添加一项工作入队"""
    def add_job(self, func, *args):
        self.work_queue.put((func, list(args)))#任务入队，Queue内部实现

    """等待所有线程运行完毕"""
    def wait_allcomplete(self):
        for item in self.threads:
            if item.isAlive(): #获取线程标识符
                item.join() #主调线程堵塞

class Work(threading.Thread): #继承Thread类
    def __init__(self, work_queue): #重写构造函数
        threading.Thread.__init__(self)
        self.work_queue = work_queue #将队列变为对象变量
        self.start() #启动

    def run(self):
        while True: #死循环，从而让创建的线程在一定条件下关闭退出
            try:
                do, args = self.work_queue.get(block=False)#从队列取数据
                do(args)
                self.work_queue.task_done()#通知系统任务完成
            except:
                break

def do_job(args):#具体要做的任务
    time.sleep(0.1)#模拟处理时间
    print threading.current_thread(), list(args)

if __name__ == '__main__':
    start = time.time()
    work_manager =  WorkManager(5,1)#或者work_manager =  WorkManager(10000, 20)
    work_manager.wait_allcomplete()
    end = time.time()
    print "cost all time: %s" % (end-start)