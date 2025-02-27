# Regular function


def square(x):

    return x**2


# Lambda function

square_lambda = lambda x: x**2

# The basic syntax of a lambda function is:
# lambda [arguments]: [expression]

# Lambda function to add two numbers

add = lambda a, b: a + b

print(add(3, 5))  # Output: 8

# Lambda function to print a name

greeting = lambda name: f"Hello, {name}!"

print(greeting("Alice"))  # Output: Hello, Alice!

# The map() function applies the given lambda function to each item in a list:
numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x**2, numbers))

print(squared)  # Output: [1, 4, 9, 16, 25]

# The filter() function creates a new list of elements for which the given lambda function returns True:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)  # Output: [2, 4, 6, 8, 10]

# The sorted() function can use a lambda function as a key for custom sorting:
students = [("Alice", "A", 15), ("Bob", "B", 12), ("Charlie", "A", 20)]

sorted_students = sorted(students, key=lambda x: x[2])

print(sorted_students)

# Output: [('Bob', 'B', 12), ('Alice', 'A', 15), ('Charlie', 'A', 20)]
