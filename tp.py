#test Queue
from multiprocessing import Queue,Process
import os,time,random

def write(q):
    print("Process to write: %s" % os.getpid())
    for value in ['A','B','C']:
        print('Put %s to queue.' % value)
        q.put(value)
        print(value,'WB:',time.time())
        time.sleep(random.random())
        print(value,'WE:',time.time())

def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value=q.get(True)
        print('Get %s from queue.' % value)
        print(value,'RE:',time.time())

if __name__=='__main__':
    q=Queue()
    pw=Process(target=write,args=(q,))
    pr=Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
#test subprocess
'''
import subprocess
p=subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output,err=p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('gbk'))
print('Exit code:',p.returncode)
'''
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
