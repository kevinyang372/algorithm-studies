import time
import threading

def background_process():
    while True:
        print("Executing background process")
        time.sleep(0.1)


if __name__ == "__main__":
    background_thread = threading.Thread(target=background_process)
    background_thread.daemon = True
    background_thread.start()

    print("Main thread executing")
    time.sleep(1)