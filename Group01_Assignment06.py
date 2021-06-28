import random
import time
import threading
from threading import Thread
from queue import Queue

queue = Queue()
threadLock = threading.Lock()
animals = ["steer","rabbit","argali","hare","lemur","cat","badger","ram","dog","crocodile"]

class Producer(Thread):
    def run(self):
        global queue
        while True:
            items = random.choice(animals)
            queue.put(items)
            threadLock.acquire()
            print ("\nItem Produced:", items)
            threadLock.release()
            time.sleep(random.random())
			
class Consumer(Thread):
    def run(self):
        global queue
        while True:
            output = queue.get()
            queue.task_done()
            threadLock.acquire()
            print("\nItem Consumed:", output)
            threadLock.release()
            time.sleep(random.random())
			
class Main():
    Producer().start()
    Producer().start()
    Consumer().start()
    Consumer().start()
    Consumer().start()
