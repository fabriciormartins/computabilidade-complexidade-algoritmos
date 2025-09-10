import time

class FibonacciMemoization:
    
    def __init__(self):
        self.memo = {}
    
    def execute(self, n):
        self.memo = {}
        start_time = time.perf_counter()
        result = self.fibonacci(n)
        end_time = time.perf_counter()
        return result, end_time - start_time
    
    def fibonacci(self, n):
        if n in self.memo:
            return self.memo[n]
        if n <= 1:
            return n
        self.memo[n] = self.fibonacci(n-1) + self.fibonacci(n-2)
        return self.memo[n]