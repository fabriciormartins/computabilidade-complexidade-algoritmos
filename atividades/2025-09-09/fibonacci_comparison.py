from fibonacci_recursive import FibonacciRecursive
from fibonacci_iterative import FibonacciIterative
from fibonacci_memoization import FibonacciMemoization

class FibonacciComparison:
    
    def __init__(self):
        self.recursive = FibonacciRecursive()
        self.iterative = FibonacciIterative()
        self.memoization = FibonacciMemoization()
    
    def compare(self, test_values):
        print(f"{'N':<5} {'Recursivo':<15} {'Iterativo':<15} {'Memoização':<15}")
        print("-" * 60)
        
        for n in test_values:
            try:
                result_rec, time_rec = self.recursive.execute(n)
                result_iter, time_iter = self.iterative.execute(n)
                result_memo, time_memo = self.memoization.execute(n)
                
                print(f"{n:<5} {time_rec:<15.6f} {time_iter:<15.6f} {time_memo:<15.6f}")
            except RecursionError:
                print(f"{n:<5} {'OVERFLOW':<15} {time_iter:<15.6f} {time_memo:<15.6f}")

# Teste
if __name__ == "__main__":
    comparison = FibonacciComparison()
    test_values = [10, 20, 30, 35, 40]
    comparison.compare(test_values)