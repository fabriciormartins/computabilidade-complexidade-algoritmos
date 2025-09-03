import time

class InsertionSort:

    def sort(self, values):
        start_time = time.perf_counter()
        steps_number = 0
        size = len(values)
        for i in range(1, size):
            steps_number += 1
            key = values[i]
            j = i - 1
            while j >= 0 and key < values[j]:
                steps_number += 1
                values[j + 1] = values[j]
                j -= 1
            values[j + 1] = key

        end_time = time.perf_counter()
        return values, end_time - start_time, steps_number
