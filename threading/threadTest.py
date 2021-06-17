import logging
import threading
import time

def thread_function(name, obj):
    logging.info("Thread %s: starting", name)
    logging.info("Thread identity: %d", threading.get_ident())
    time.sleep(10)
    logging.info("Thread %s: finishing on %s", name, obj)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,'a',), daemon=True)
    # x = threading.Thread(target=thread_function, args=(1, 'a',), daemon=False)
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    x.join()
    logging.info("Main    : all done")


"""
here is the log if we 
1. set daemon=False
2. comment out x.join() on line 22

05:34:32: Main    : before creating thread
05:34:32: Main    : before running thread
05:34:32: Thread 1: starting
05:34:32: Main    : wait for the thread to finish
05:34:32: Main    : all done
05:34:34: Thread 1: finishing

"""


