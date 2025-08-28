from binarysearch import BinarySearch
from linearsearch import LinearSearch
from values_generator import NumberGenerator 

bs = BinarySearch()
generator = NumberGenerator()

search_value, values = generator.generate(500)

print(f"Search value: {search_value}")
print(f"Values: ", *values)
print()
print()
print()

index_bs, time_bs, steps_bs = bs.search(values, search_value)

print('Binary Search Results')
print(f"The index of value in array is {index_bs} and the value searched is {values[index_bs]}.")
print(f"Steps: {steps_bs}")
print(f"Time: {time_bs} seconds")

print()
ls = LinearSearch()
index_ls, time_ls, steps_ls = ls.search(values, search_value)
print('Linear Search Results')
print(f"The index of value in array is {index_ls} and the value searched is {values[index_ls]}.")
print(f"Steps: {steps_ls}")
print(f"Time: {time_ls} seconds")