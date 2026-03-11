from util import custom_search
from algorithms.search import BinarySearch, LinearSearch

search_functions = [BinarySearch, LinearSearch]
sorted_list =[1,1,1,1,1,1,2,2,4,4,4,4,4,4,4]
expected_result=[-1, 0, 6, -1, 8, -1]

def sorted_list_test(sorted_list, expected_result, search_functions):
    for search_function in search_functions:
        print(f"Testing {search_function.__name__}")
        for i in range(6):
            target = i
            expected_index = expected_result[i]
            print(f"Testing {i}")
            result = custom_search(sorted_list, target, search_function)
            assert result == expected_index, f"Test Failed: Expected {expected_index}, got {result}"
    print("All expected list tests passed!")

string = "nsfw"

def string_tests(string, search_function):
    c = 0
    for letter in string:
        result = LinearSearch.search(string, letter)
        assert result == c, f"Test Failed: Expected {c}, got {result}"
        c += 1
    print("String tests passed.")

print(custom_search(sorted_list, 1, LinearSearch))
print(custom_search(sorted_list, 2, LinearSearch))
print(custom_search(sorted_list, 4, LinearSearch))
# exit()
sorted_list_test(sorted_list, expected_result, search_functions)
string_tests(string, LinearSearch)