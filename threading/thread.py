import threading

def do_something():
    print("doing something")

thread = threading.Thread(target=do_something)

thread.start()

thread.join()
