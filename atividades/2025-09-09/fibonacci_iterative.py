import time

class FibonacciIterative:
    
    def execute(self, n):
        start_time = time.perf_counter()
        result = self.fibonacci(n)
        end_time = time.perf_counter()
        return result, end_time - start_time
    
    def fibonacci(self, n):
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b