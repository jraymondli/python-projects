import time
import concurrent.futures

e = concurrent.futures.ThreadPoolExecutor(4)
s = range(10)
for i in e.map(time.sleep, s):
    print(s, i)

