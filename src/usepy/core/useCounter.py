from typing import Optional
import threading


class useCounter:

    def __init__(self,
                 init_value: int = 1,
                 min_value: Optional[int] = None,
                 max_value: Optional[int] = None):
        self.init_value = init_value
        self.count = init_value
        self.min_value = float('-inf') if min_value is None else min_value
        self.max_value = float('inf') if max_value is None else max_value
        self._lock = threading.Lock()

    def inc(self, delta: int = 1):
        with self._lock:
            self.count = min(self.max_value, self.count + delta)

    def dec(self, delta: int = 1):
        with self._lock:
            self.count = max(self.min_value, self.count - delta)

    def get(self):
        with self._lock:
            return self.count

    def set(self, value):
        with self._lock:
            self.count = max(self.min_value, min(self.max_value, value))

    def reset(self, value: Optional[int] = None):
        with self._lock:
            self.set(value or self.init_value)
