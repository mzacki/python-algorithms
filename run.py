from algo.search.binary.binary_search import binary_search
from algo.sort.quick.quick_sort import quick_sort
from algo.sort.selection.selection_sort import selection_sort

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))  # => 1 (index of 3 in the array)
print(binary_search(my_list, -1))  # => none

unsorted_list = [9, 3, 4, 8, 2, 1]
print(selection_sort(unsorted_list))  # => returns sorted list
print(quick_sort([1, 0, 0]))
