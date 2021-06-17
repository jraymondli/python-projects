import concurrent.futures
import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    logging.info("Thread identity: %d", threading.get_ident())
    time.sleep(2)
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        # 1, 2, 3 got mapp ed to name in thread_function parameter
        executor.map(thread_function, range(3))
        # using array to map paramter instead
        executor.map(thread_function, ['a', 'b', 'c'])
        # executor.submit(thread_function, range(3))

    logging.info("All completed!")