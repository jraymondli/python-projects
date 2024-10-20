import concurrent.futures
import logging
import time
import threading

class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def update(self, name):
        logging.info("Thread %s: starting update", name)
        logging.debug("Thread %s about to lock")

        if "lock" in sys.argv:
            # race condition fixed if we lock
            with self._lock:
                local_copy = self.value
                local_copy += 1
                time.sleep(0.1)
                self.value = local_copy
        else:
            # race condition if we do the following
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
        logging.debug("Threading %s after release", name)
        logging.info("Thread %s: finishing update", name)


if __name__ == "__main__":
    import sys
    print(sys.argv)

    myformat = "%(asctime)s: %(message)s"
    logging.basicConfig(format=myformat, level=logging.DEBUG,
                        datefmt="%H:%M:%S")
    # logging.getLogger().setLevel(logging.DEBUG)
    database = FakeDatabase()
    logging.info("Testing update. Starting value is %d.", database.value)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.update, index)
    logging.info("Testing update. Ending value is %d.", database.value)



