# 4月11日
# import os
#
# print('process(%s) is running'%os.getpid())
#
# pid=os.fork()
#
# if pid == 0:
#     print('I am child process(%s) and my parement process is %s'%(os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s)'%(os.getpid(), pid))



print()
import os
from multiprocessing import Process


def run_proc(name):
    print('Run child process %s(%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s' % os.getpid())
    p = Process(target=run_proc, args=('test',))  # 为什么加逗号就可以,不加逗号就会报错
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

# 4月13日
print()
from multiprocessing import Pool
import random, time, os


def long_run_time(name):
    print('Run task%s(%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s' % os.getpid())
    # print('Waiting for all sunprocess done1.')
    p = Pool(4)  # 这里改成5就可以同时跑5个进程了
    for i in range(5):
        # p.apply(long_run_time, args=(i,))# 这个语句跟下面的语句同样意思,都是表示所有参数
        # p.apply(long_run_time, [i])
        p.apply_async(long_run_time, args=(i,))  # 与上面相比,这个是异步非阻塞,不等待当前进程完毕就能根据系统调度进行下一个进程的开始
    print('Waiting for all sunprocess done.')  # 为什么这个会在子进程执行之前执行??原因在上面
    p.close()  # close之后就不能再生成新的Proce进程对象了
    p.join()  # 告诉主进程等子进程运行完毕后再运行下面的进程,close()一定要放在join()前面
    print('All subprocess done.')


