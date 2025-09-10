import time

class FibonacciRecursive:
    
    def execute(self, n):
        start_time = time.perf_counter()
        result = self.fibonacci(n)
        end_time = time.perf_counter()
        return result, end_time - start_time
    
    def fibonacci(self, n):
        if n <= 1:
            return n
        return self.fibonacci(n-1) + self.fibonacci(n-2)