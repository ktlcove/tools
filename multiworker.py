#!/usr/bin/env python3
#
# create_date : 2015-1?-?? i forget
# author : ktlcove
# mail : ktl_cove@126.com

import threading
import queue
import time

class Worker():

    works = queue.Queue()
    lock = threading.Lock()

    def __init__(self,worker_count=5,queue_size=20,wait_queue=None):
        self.workers = {}
        self.worker_count = worker_count
        self.works.maxsize = queue_size
        self.wait_queue = wait_queue

    def scheduler(self):
        while self.wait_queue.not_empty:
            if self.works.not_full:
                self.works.put(self.wait_queue.get())
        # print ('scheduler return')
        return

    def work(self,wid):
        while self.workers[wid]['status'] is not True:
            if self.works.not_empty:
                self.lock.acquire()
                ( work , args ,kwargs ) = self.works.get()
                self.lock.release()
                try:
                   work(*args,**kwargs)
                except:
                   print ('error')
            if self.wait_queue.empty() and self.works.empty():
                self.workers[wid]['status'] = True
                # print (wid,'return')
                return

    def start(self):
        self.bind = threading.Thread(target=self.scheduler,daemon=True)
        self.bind.start()
        for i in range(self.worker_count):
            self.workers[i] = {}
            self.workers[i]['worker'] = threading.Thread(target=self.work,args=(i,),daemon=False)
            self.workers[i]['status'] = None 
        for wid in self.workers.keys():
            self.workers[wid]['worker'].start()
        return

# eg
if __name__ == "__main__":
    
    class a():
         l = 1
         # eg function
         def pp(self,r,b=1):
             print (self.l)
             print (r,b)
             time.sleep(0.2)

    # empty queue
    q = queue.Queue()
    
    aa = a()

    # build work queue
    for i in range(100):
        q.put((aa.pp,(i,),{'b':1}))

    # init multworker queue
    # work_count : how many work threading start
    # queue_size : one time how many work wait to begin
    # wait_queue : all works in this queue
    S = Worker(worker_count=5,queue_size=20,wait_queue=q)
    # start work
    S.start()
