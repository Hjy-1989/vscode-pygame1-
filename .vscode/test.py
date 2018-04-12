import os
from multiprocessing import process

def run_proc(name):
    print ('child process %s(%s) running...'%(name,os.getpid()))
if __name__=="__main__":
    print ('Parents process %s.'%os.getpid())
    for i in range(5):
        p=process(target=run_proc,args=(str(i),))
        print ('process will start.')
        p.start()
    p.join()
    print ('process end.')