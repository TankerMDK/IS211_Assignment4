import time
import random

def get_me_random_list(n):
    """Generate list of n elements in random order"""
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list

# The Sorting Functions

def insertion_sort(a_list):
    start = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position -= 1
        a_list[position] = current_value
    return time.time() - start

def shell_sort(a_list):
    start = time.time()
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        sublist_count //= 2
    return time.time() - start

def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position -= gap
        a_list[position] = current_value

def python_sort(a_list):
    start = time.time()
    sorted_list = sorted(a_list)
    return time.time() - start

# The Main Function
if __name__ == "__main__":
    sizes = [500, 1000, 5000]
    sort_functions = [insertion_sort, shell_sort, python_sort]

    for size in sizes:
        print(f"\nList size: {size}")
        for sort_func in sort_functions:
            total_time = 0
            for _ in range(100):
                mylist = get_me_random_list(size)
                time_spent = sort_func(mylist)
                total_time += time_spent
            avg_time = total_time / 100
            print(f"{sort_func.__name__.replace('_', ' ').title()} took {avg_time:10.7f} seconds to run, on average")
