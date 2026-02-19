import queue
import threading

class EventQueue:
    def __init__(self):
        self.queue = queue.Queue()
        self.lock = threading.Lock()

    def enqueue(self, event):
        with self.lock:
            self.queue.put(event)

    def dequeue(self):
        with self.lock:
            if not self.queue.empty():
                return self.queue.get()
            return None

    def is_empty(self):
        with self.lock:
            return self.queue.empty()

    def size(self):
        with self.lock:
            return self.queue.qsize()