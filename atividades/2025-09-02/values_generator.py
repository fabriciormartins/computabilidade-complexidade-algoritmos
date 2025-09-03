import random

class NumberGenerator:

    """
    Generate an ordered array of integers from 1 to 10,000,000.
    This class is designed to be used as an iterator.
    """
    def generate(self, max_size):
        numbers = set(())
        
        size = 0
        while size < max_size:
             size = len(numbers)
             number = self.generate_number()
             numbers.add(number)
        return ( number , sorted(numbers))
    
    def generate_unsorted(self, max_size):
        numbers = set(())
        
        size = 0
        while size < max_size:
             size = len(numbers)
             number = self.generate_number()
             numbers.add(number)
        return ( number , numbers)

    def generate_number(self, max_range=10000):
        return random.randint(0, max_range)