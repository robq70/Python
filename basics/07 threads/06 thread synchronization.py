import threading, time

data = ["Adam", "Ola", "Kasia", "Daniel", "Rafał"]
dataLock = threading.Lock()


class someThread(threading.Thread):
    def __init__(self, threadName, dataLen, sleepTime):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.dataLen = dataLen
        self.sleepTime = sleepTime

    def run(self):
        num = 0
        while num < self.dataLen:
            dataLock.acquire()
            data[num] = data[num] + " " + str(num)
            print(self.threadName, data[num])
            dataLock.release()

            time.sleep(self.sleepTime)

            num += 1
        print(self.threadName, " ended")


t1 = someThread("T1", len(data), 0.1)
t2 = someThread("THREAD 2", len(data), 0.3)
t3 = someThread("thread 3", len(data), 0.4)

t1.start()
t2.start()
t3.start()

time.sleep(1)
print("-- Thread 2 status: ", t2.is_alive())

t1.join()
t2.join()
t3.join()

print("All threads ended")
