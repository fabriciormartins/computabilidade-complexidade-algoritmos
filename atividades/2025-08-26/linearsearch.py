import time

class LinearSearch:
    def search(selft, values, searchedValue):
        start_time = time.perf_counter()
        steps_number = 0
        for i in range(len(values)):
            steps_number += 1
            if values[i] == searchedValue:
                end_time = time.perf_counter()
                steps_number+1
                return (i, end_time - start_time, steps_number)
        end_time = time.perf_counter()
        return (-1, end_time - start_time, steps_number)
