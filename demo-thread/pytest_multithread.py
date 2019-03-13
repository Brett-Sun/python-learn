import _thread, time

mutex = _thread.allocate_lock()

def counter(myId, count):
    for i in range(count):
        time.sleep(1)
        mutex.acquire()
        print("[%s] => count %s \n" % (myId, i))
        mutex.realse()

for i in range(5):
    _thread.start_new_thread(counter, (i, 5))

time.sleep(10)
print("********Main thread finished*************8")