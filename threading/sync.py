import threading

lock = threading.Lock()
shared_resource = 0

def increment_resource():
    global shared_resource
    with lock:  # Ensures that only one thread modifies shared_resource at a time
        temp = shared_resource
        temp += 1
        shared_resource = temp
        print(f"Shared resource incremented to {shared_resource}")

threads = [threading.Thread(target=increment_resource) for _ in range(50)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
