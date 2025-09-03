from values_generator import NumberGenerator
from bubble_sort import BubbleSort
from merge_sort import MergeSort
from insertion_sort import InsertionSort


generator = NumberGenerator()
bs = BubbleSort()
_, values = generator.generate_unsorted(10000)

print("\n" * 3)
# print(f"Values: ", *values)
print("\n" * 3)

bubble_sort_values = [*values]

ordered_by_bubble_sort, time_bs, steps_bs = bs.sort(bubble_sort_values)

print('Bubble Sort Results')
# print(f"Sorted Values: ", *ordered_by_bubble_sort)
print(f"Steps: {steps_bs}")
print(f"Time: {time_bs} seconds")
print("\n" * 3)


merge_sort_values = [*values]
print("\n" * 3)
ms = MergeSort()
ordered_by_merge_sort, time_ms, steps_ms = ms.sort(merge_sort_values)
print('Merge Sort Results')
# print(f"Sorted Values: ", *ordered_by_merge_sort)
print(f"Steps: {steps_ms}")
print(f"Time: {time_ms} seconds")


insertion_sort_values = [*values]
print("\n" * 3)
iss = InsertionSort()
ordered_by_insertion_sort, time_iss, steps_iss = iss.sort(insertion_sort_values)
print('Insertion Sort Results')
# print(f"Sorted Values: ", *ordered_by_insertion_sort)
print(f"Steps: {steps_iss}")
print(f"Time: {time_iss} seconds")
