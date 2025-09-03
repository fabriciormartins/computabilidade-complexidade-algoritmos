import time

class MergeSort:
  start_time, steps_number = 0, 0
  def sort(self, values):
    self.start_time = time.time()
    self.steps_number = 0
    self.merge_sort(values)
    end_time = time.time()
    return values, (end_time - self.start_time), self.steps_number
  def merge_sort(self, values):
    if len(values) <= 1:
      return values
    mid = len(values) // 2
    left = values[:mid]
    right = values[mid:]
    self.merge_sort(left)
    self.merge_sort(right)
    self.merge(left, right, values)
    return values
  
  def merge(self, left, right, values):
    i = j = k = 0
    while i < len(left) and j < len(right):
      self.steps_number += 1
      if left[i] < right[j]:
        values[k] = left[i]
        i += 1
      else:
        values[k] = right[j]
        j += 1
      k += 1
      self.steps_number += 1
      while i < len(left):
        self.steps_number += 1
        values[k] = left[i]
        i += 1
        k += 1
        self.steps_number += 1
        while j < len(right):
          self.steps_number += 1
          values[k] = right[j]
          j += 1
          k += 1
          self.steps_number += 1
          return values