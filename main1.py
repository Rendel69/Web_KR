#number_1: int = 12
#numder_2 = 15.5
#print(number_1,
#      numder_2,
#      )
#string_1 = 'hello "world"'
#string_2 = "hello 'world'"
#string_3 = "hello \"world\""
#string_4 = "\n"
#print(
# string_1,
#  string_4,
#   string_2,
#    string_4,
#    string_3
#)
def add_numbers(a, b):
    return a + b
result = add_numbers(3, 5)
print(result)


def sum_of_list(numbers):
    return sum(numbers)
result = sum_of_list([1, 2, 3, 4, 5])
print(result)

def join_strings(separator, *strings):
    return separator.join(strings)
result = join_strings(", ", "яблоко", "банан", "кокос")
print(result)

def split_string(input_string, delimiter):
    return input_string.split(delimiter)
result = split_string("яблоко,банан,кокос", ",")
print(result)