import time


class BubbleSort:

 def sort(self,values):
    start_time = time.perf_counter()
    steps_number = 0
    size = len(values)
    if(size == 0):
        steps_number += 1
        end_time = time.perf_counter()
        return (values, end_time - start_time, steps_number)
    has_modification = True
    for i in range(size):
        steps_number += 1
        if not has_modification:
            break
        has_modification = False
        for j in range(size - 1 - i):
            steps_number += 1
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                has_modification = True
    end_time = time.perf_counter()
    return values, end_time - start_time, steps_number