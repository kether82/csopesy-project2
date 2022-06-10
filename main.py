import threading
import time
import random
from collections import deque 

exitFlag = 0

class slot (threading.Thread):
   def __init__(self, threadID, customers):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.customers = customers
      self.color = None
   def run(self):
    print ("Starting " + str(self.threadID))
    while not exitFlag:
      mutexQueue.acquire()
      if customers:
        #  data = customers.get()
        #  mutexQueue.release()
        #  print ("%s processing %s" % (threadName, data))
        customer = customers[0]
        customers.popleft()
        mutexQueue.release()
        # print(str(self.color) + "\n")
        if(customer[0] == self.color):
            # same color
            print("\n" + str(customer[0]) + " ID:" + str(customer[1])+" Slot:"+str(self.threadID))
        elif(self.color == None):
            # first color
            print("\n" + customer[0] + " Only" + "\n" + str(customer[0]) + " ID:" + str(customer[1])+" Slot:"+str(self.threadID))
            self.color = customer[0]
        else:
            # different color
            print("\n" + "Empty fitting room")
            self.color = None
            customers.appendleft(customer)
      else:
        #  mutexQueue.release()
        print ("Exiting Slot:" + str(self.threadID))

# class myThread (threading.Thread):
#    def __init__(self, threadID, name, q):
#       threading.Thread.__init__(self)
#       self.threadID = threadID
#       self.name = name
#       self.q = q
#    def run(self):
#       print ("Starting " + self.name)
#       process_data(self.name, self.q)
#       print ("Exiting " + self.name)

# def process_data(threadName, q):
#    while not exitFlag:
#       queueLock.acquire()
#       if not workQueue.empty():
#          data = q.get()
#          queueLock.release()
#          print ("%s processing %s" % (threadName, data))
#       else:
#          queueLock.release()
#          time.sleep(1)

# n , b, g = input("Enter n, b, g: ").split()

# n = int(n)
# b = int(b)
# g = int(g)

n = 2
b = 4
g = 6
# threadList = ["Thread-1", "Thread-2", "Thread-3"]
# nameList = ["One", "Two", "Three", "Four", "Five"]
mutexQueue = threading.Lock()
customers = []
slots = []
threadID = 1

# Create new threads
# for tName in threadList:
#    thread = myThread(threadID, customer)
#    thread.start()
#    threads.append(thread)
#    threadID += 1


# Fill the queue
# mutexQueue.acquire()
for customer in range(b):
   customers.append(("blue", customer))
for customer in range(g):
    customers.append(("green", customer))
random.shuffle(customers)
customers = deque(customers)
# mutexQueue.release()

for x in range(n):
    thread = slot(x, customers)
    thread.start()
    slots.append(thread)




# queueLock.acquire()
# for word in nameList:
#    workQueue.put(word)
# queueLock.release()

# Wait for queue to empty
while customers:
   pass

# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete
for t in slots:
   t.join()
print ("Exiting Main Thread")