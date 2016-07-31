#test subprocess
import subprocess
r=subprocess.call(['ipython','--version'])
print('Exit code:',r)
#test thread and process
'''
from multiprocessing import Process
from multiprocessing import Pool
import os,time,random

def run_proc(name):
    print('Run child process %s (%s)...' % (name,os.getpid()))
    start=time.time()
    time.sleep(random.random()*3)
    stop=time.time()
    print('Task %s run %0.3f seconds' % (name,(stop-start)))

if __name__=='__main__':
    print('Father process {0}.'.format(os.getpid()))
    ts=time.time()
    p=Pool()
    print("Child process will start.")
    for i in range(9):
        p.apply_async(run_proc,args=(i,))
    print('Waiting for the subprocessings.')
    p.close()
    p.join()
    print('Everything ended.')
    te=time.time()
    print("Totally %0.3f seconds" % (te-ts))
'''
