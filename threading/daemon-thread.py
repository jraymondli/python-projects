import threading
import time

def background_task():
    while True:
        print("Background task is running...")
        time.sleep(1)

# Create a daemon thread
thread = threading.Thread(target=background_task)
thread.daemon = True
thread.start()

# Main thread will exit after 5 seconds, stopping the background task
time.sleep(5)
print("Main thread is done.")
