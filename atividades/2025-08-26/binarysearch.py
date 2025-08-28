import time

class BinarySearch:
    def search(self, values, searchedValue):
      start_time = time.perf_counter()
      size = len(values)
      right = size - 1
      left = 0
      steps_number = 0
      while left <= right:
        steps_number += 1
        middle = (left + right) // 2
        if values[middle] == searchedValue:
         end_time = time.perf_counter()
         return (middle, end_time - start_time, steps_number)
        elif values[middle] < searchedValue:
           steps_number += 1
           left = middle + 1
        else:
           steps_number += 1
           right = middle - 1
      end_time = time.perf_counter()
      return (-1, end_time - start_time, steps_number)
