#!/usr/bin/env python
#coding:utf-8
__author__ = '123'

'''
IO多路复用

    I/O多路复用指：通过一种机制，可以监视多个描述符，一旦某个描述符就绪（一般是读就绪或者写就绪），能够通知程
序进行相应的读写操作。目前支持I/O多路复用的系统调用有 select，poll，epoll

应用场景：
    服务器需要同时处理多个处于监听状态或者多个连接状态的套接字。
    服务器需要同时处理多种网络协议的套接字。

#!/usr/bin/python
# -*- coding: utf-8 -*-
import select
import socket
import Queue

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setblocking(False)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR , 1)
server_address= ('192.168.1.5',8080)
server.bind(server_address)
server.listen(10)

#select轮询等待读socket集合
inputs = [server]
#select轮询等待写socket集合
outputs = []
message_queues = {}
#select超时时间
timeout = 20

while True:
    print "等待活动连接......"
    readable , writable , exceptional = select.select(inputs, outputs, inputs, timeout)

    if not (readable or writable or exceptional) :
        print "select超时无活动连接，重新select...... "
        continue;
    #循环可读事件
    for s in readable :
        #如果是server监听的socket
        if s is server:
            #同意连接
            connection, client_address = s.accept()
            print "新连接： ", client_address
            connection.setblocking(0)
            #将连接加入到select可读事件队列
            inputs.append(connection)
            #新建连接为key的字典，写回读取到的消息
            message_queues[connection] = Queue.Queue()
        else:
            #不是本机监听就是客户端发来的消息
            data = s.recv(1024)
            if data :
                print "收到数据：" , data , "客户端：",s.getpeername()
                message_queues[s].put(data)
                if s not in outputs:
                    #将读取到的socket加入到可写事件队列
                    outputs.append(s)
            else:
                #空白消息，关闭连接
                print "关闭连接：", client_address
                if s in outputs :
                    outputs.remove(s)
                inputs.remove(s)
                s.close()
                del message_queues[s]
    for s in writable:
        try:
            msg = message_queues[s].get_nowait()
        except Queue.Empty:
            print "连接：" , s.getpeername() , '消息队列为空'
            outputs.remove(s)
        else:
            print "发送数据：" , msg , "到", s.getpeername()
            s.send(msg)

    for s in exceptional:
        print "异常连接：", s.getpeername()
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
        del message_queues[s]
'''

'''
    进程和线程的区别和关系：

    对于操作系统来说，一个任务就是一个进程（Process），比如打开一个浏览器就是启动一个浏览器进程，打开一个记事
本就启动了一个记事本进程，打开两个记事本就启动了两个记事本进程，打开一个Word就启动了一个Word进程。
    有些进程还不止同时干一件事，比如Word，它可以同时进行打字、拼写检查、打印等事情。在一个进程内部，要同时干多
件事，就需要同时运行多个“子任务”，我们把进程内的这些“子任务”称为线程（Thread）。
    由于每个进程至少要干一件事，所以，一个进程至少有一个线程。当然，像Word这种复杂的进程可以有多个线程，多个线
程可以同时执行，多线程的执行方式和多进程是一样的，也是由操作系统在多个线程之间快速切换，让每个线程都短暂地交替
运行，看起来就像同时执行一样。当然，真正地同时执行多线程需要多核CPU才可能实现。
    线程是最小的执行单元，而进程由至少一个线程组成。如何调度进程和线程，完全由操作系统决定，程序自己不能决定什
么时候执行，执行多长时间。
'''

'''
python的进程

    multiprocessing包的组件Process, Queue, Pipe, Lock等组件提供了与多线程类似的功能。使用这些组件，可以方便
地编写多进程并发程序。
'''

'''
Queue队列

    Queue是多进程安全的队列，可以使用Queue实现多进程之间的数据传递。put方法用以插入数据到队列中，put方法还有
两个可选参数：blocked和timeout。如果blocked为True（默认值），并且timeout为正值，该方法会阻塞timeout指定的时
间，直到该队列有剩余的空间。如果超时，会抛出Queue.Full异常。如果blocked为False，但该Queue已满，会立即抛出
Queue.Full异常。

    get方法可以从队列读取并且删除一个元素。同样，get方法有两个可选参数：blocked和timeout。如果blocked为True
（默认值），并且timeout为正值，那么在等待时间内没有取到任何元素，会抛出Queue.Empty异常。如果blocked为False，
有两种情况存在，如果Queue有一个值可用，则立即返回该值，否则，如果队列为空，则立即抛出Queue.Empty异常。



from multiprocessing import Process, Queue

def offer(queue):
    queue.put("Hello World")

if __name__ == '__main__':
    q = Queue()
    p = Process(target=offer, args=(q,))
    p.start()
    print q.get()
'''

'''
Pipes管道

    Pipe方法返回(conn1, conn2)代表一个管道的两个端。Pipe方法有duplex参数，如果duplex参数为True(默认值)那么
这个管道是全双工模式，也就是说conn1和conn2均可收发。duplex为False，conn1只负责接受消息，conn2只负责发送消息
    send和recv方法分别是发送和接受消息的方法。例如，在全双工模式下，可以调用conn1.send发送消息，conn1.recv接
收消息。如果没有消息可接收，recv方法会一直阻塞。如果管道已经被关闭，那么recv方法会抛出EOFError。

from multiprocessing import Process, Pipe

def send(conn):
    conn.send("Hello World")
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=send, args=(child_conn,))
    p.start()
    print parent_conn.recv()
'''

'''
创建进程示例

#!/usr/bin/env python
# -*- coding:utf-8 -*-
from multiprocessing import Process
import os

def run_proc(name):
    print 'Run child process %s (%s)...' % (name, os.getpid())

if __name__=='__main__':
    print 'Parent process %s.' % os.getpid()
    p = Process(target=run_proc, args=('test',))
    print 'Process will start.'
    p.start()
    print 'Process end.'
创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动。
注意：由于进程之间的数据需要各自持有一份，所以创建进程需要的非常大的开销。
'''

'''
进程锁示例

from multiprocessing import Process, Array, RLock
def Foo(lock,temp,i):
    """
    将第0个数加100
    """
    lock.acquire()
    temp[0] = 100+i
    for item in temp:
        print i,'----->',item
    lock.release()

lock = RLock()
temp = Array('i', [11, 22, 33, 44])

for i in range(20):
    p = Process(target=Foo,args=(lock,temp,i,))
    p.start()
'''

'''
进程池示例

    在利用Python进行系统管理的时候，特别是同时操作多个文件目录，或者远程控制多台主机，并行操作可以节约大量的时
间。当被操作对象数目不大时，可以直接利用multiprocessing中的Process动态成生多个进程，十几个还好，但如果是上百
个，上千个目标，手动的去限制进程数量却又太过繁琐，此时可以发挥进程池的功效。
    Pool可以提供指定数量的进程供用户调用，当有新的请求提交到pool中时，如果池还没有满，那么就会创建一个新的进程
用来执行该请求；但如果池中的进程数已经达到规定最大值，那么该请求就会等待，直到池中有进程结束，才会创建新的进程
来它。

#!/usr/bin/env python
#coding:utf-8
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))

if __name__=='__main__':
    print 'Parent process %s.' % os.getpid()
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print 'Waiting for all subprocesses done...'
    p.close()
    p.join()
    print 'All subprocesses done.'
join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行，这是因为Pool的默认大小在我的电脑上是4，
因此，最多同时执行4个进程。
'''

'''
进程间共享数据

#!/usr/bin/env python
# -*- coding:utf-8 -*-
from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码:
def write(q):
    for value in ['A', 'B', 'C']:
        print 'Put %s to queue...' % value
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    while True:
        value = q.get(True)
        print 'Get %s from queue.' % value

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
进程间默认无法共享数据


'''

'''
Python的线程

    多任务可以由多进程完成，也可以由一个进程内的多线程完成。进程是由若干线程组成的，一个进程至少有一个线程。
    Python的标准库提供了两个模块：thread和threading，thread是低级模块，threading是高级模块，对thread进行了
封装。绝大多数情况下，我们只需要使用threading这个高级模块。启动一个线程就是把一个函数传入并创建Thread实例，然
后调用start()开始执行
'''

'''
python的多线程模块：threading

    Thread                  #线程执行的对象

        start               线程准备就绪，等待CPU调度
        setName             为线程设置名称
        getName             获取线程名称  
        setDaemon           设置为后台线程或前台线程（默认）
                            如果是后台线程，主线程执行过程中，后台线程也在进行，主线程执行完毕后，后台线程不
                            论成功与否，均停止如果是前台线程，主线程执行过程中，前台线程也在进行，主线程执行
                            完毕后，等待前台线程也执行完成后，程序停止
        join                逐个执行每个线程，执行完毕后继续往下执行，该方法使得多线程变得无意义
        run                 线程被cpu调度后执行Thread类对象的run方法
    Rlock                   #线程锁：可重入锁对象.使单线程可以在此获得已获得了的锁(递归锁定)

        acquire             为线程加锁
        release             为线程解锁
    Event                   #python线程的事件用于主线程控制其他线程的执行。

        set                 将全局变量设置为True
        wait                事件处理的机制：全局定义了一个“Flag”，如果“Flag”值为 False，那么当程序执行
                            event.wait方法时就会阻塞，如果“Flag”值为True，那么event.wait 方法时便不再阻塞
        clear               将全局变量设置为False
    Semaphore               为等待锁的线程提供一个类似等候室的结构
    BoundedSemaphore        与Semaphore类似,只是不允许超过初始值
    Time                    与Thread相似,只是他要等待一段时间后才开始运行
    activeCount()           当前活动的线程对象的数量
    currentThread()         返回当前线程对象
    enumerate()             返回当前活动线程的列表
    settrace(func)          为所有线程设置一个跟踪函数
    setprofile(func)        为所有线程设置一个profile函数



'''

'''
线程示例

#!/usr/bin/env python
#coding:utf-8
import threading
import time

def show(arg):
    time.sleep(1)
    print 'thread'+str(arg)

for i in range(10):
    t = threading.Thread(target=show, args=(i,))
    t.start()
print 'main thread stop'
'''

'''
线程锁示例

    多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，
所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个
线程同时改一个变量，把内容给改乱了。

#!/usr/bin/env python
#coding:utf-8
import threading
import time
gl_num = 0
def show(arg):
    global gl_num
    time.sleep(1)
    gl_num +=1
    print gl_num

for i in range(10):
    t = threading.Thread(target=show, args=(i,))
    t.start()
print 'main thread stop'

由于线程之间是进行随机调度，并且每个线程可能只执行n条执行之后，CPU接着执行其他线程
如果按上例的话会出现一种情况多个线程同时修改一份内存资源，造成数据的修改混乱那么线程锁可以解决这个问题
#!/usr/bin/env python
#coding:utf-8import threading
import time
gl_num = 0
lock=threading.RLock()
def show(arg):
    lock.acquire()
    global gl_num
    time.sleep(1)
    gl_num +=1
    print gl_num
    lock.release()
for i in range(10):
    t = threading.Thread(target=show, args=(i,))
    t.start()
print 'main thread stop'

    因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，任何Python
线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全
局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也
只能用到1个核。
    GIL是Python解释器设计的历史遗留问题，通常我们用的解释器是官方实现的CPython，要真正利用多核，除非重写一个
不带GIL的解释器。所以，在Python中，可以使用多线程，但不要指望能有效利用多核。如果一定要通过多线程利用多核，那
只能通过C扩展来实现，不过这样就失去了Python简单易用的特点。
    不过，也不用过于担心，Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有
各自独立的GIL锁，互不影响。
    多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。
    Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。
'''

'''
线程的事件示例

#!/usr/bin/env python
# -*- coding:utf-8 -*-
import threading

def do(event):
    print 'start'
    event.wait()
    print 'execute'

event_obj = threading.Event()
for i in range(10):
    t = threading.Thread(target=do, args=(event_obj,))
    t.start()

event_obj.clear()
inp = raw_input('input:')
if inp == 'true':
    event_obj.set()
'''

'''
协程简介

    线程和进程的操作是由程序触发系统接口，最后的执行者是系统；协程的操作则是程序员。
    协程存在的意义：对于多线程应用，CPU通过切片的方式来切换线程间的执行，线程切换时需要耗时（保存状态，下次继
续）。协程，则只使用一个线程，在一个线程中规定某个代码块执行顺序。
    协程的适用场景：当程序中存在大量不需要CPU的操作时（IO），适用于协程；
'''

'''
协程示例

#!/usr/bin/env python
# -*- coding:utf-8 -*-
from greenlet import greenlet

def test1():
    print 12
    gr2.switch()
    print 34
    gr2.switch()

def test2():
    print 56
    gr1.switch()
    print 78

gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()
'''

'''
进程vs线程

    我们可以把任务分为计算密集型和IO密集型。
    计算密集型任务的特点是要进行大量的计算，消耗CPU资源，比如计算圆周率、对视频进行高清解码等等，全靠CPU的运算
能力。这种计算密集型任务虽然也可以用多任务完成，但是任务越多，花在任务切换的时间就越多，CPU执行任务的效率就越
低，所以，要最高效地利用CPU，计算密集型任务同时进行的数量应当等于CPU的核心数。
    计算密集型任务由于主要消耗CPU资源，因此，代码运行效率至关重要。用Python的话适合多进程
第二种任务的类型是IO密集型，涉及到网络、磁盘IO的任务都是IO密集型任务，这类任务的特点是CPU消耗很少，任务的大部
分时间都在等待IO操作完成（因为IO的速度远远低于CPU和内存的速度）。对于IO密集型任务，任务越多，CPU效率越高，但也
有一个限度。常见的大部分任务都是IO密集型任务，比如Web应用。这时候不需要cpu做过多的计算，应当用多线程。

'''
