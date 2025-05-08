# Day 3 is
# [ ] Day 3: Work with functions, lists, dictionaries, sets
# python  def keywords

# defining function
def fun1():
    print("Hello")

# calling function
fun1()

#Example 1: Create function to find the subtraction of two Numbers
# Python3 code to demonstrate
# def keyword

# function for subtraction of 2 numbers.
def subNumbers(x, y):
    return (x-y)

# main code
a = 90
b = 50

# finding subtraction
res = subNumbers(a, b)

# print statement
print("subtraction of ", a, " and ", b, " is ", res)



# Example 2: Create function with the first 10 prime numbers
# Python program to print first 10 prime numbers

# A function name prime is defined
# using def

def fun(n):
    x = 2
    count = 0
    while count < n:
        for d in range(2, int(x ** 0.5) + 1):  # check divisibility only up to sqrt(x)
            print("d----",d)
            if x % d == 0:
                break  # if divisible, it's not prime, so break the loop
        else:
            print(x)  # prime number
            count += 1
        x += 1

# Driver Code
n = 10

fun(n)


# Passing Function as an Argument
# A function that takes another function as an argument
def fun(func, arg):
    return func(arg)

def square(x):
    return x ** 2

# Calling fun and passing square function as an argument
res = fun(square, 5)
print(res)



# Python def keyword example with *args
def fun(*args):
    for arg in args:
        print(arg)

# Calling the function with multiple arguments
fun(1, 2, 3, 4, 5)


# Python def keyword example with **kwargs
def fun(**kwargs):
    for k, val in kwargs.items():
        print(f"{k}: {val}")

# Calling the function with keyword arguments
fun(name="Alice", age=30, city="New York")


#2. Lists
#len(), min(), max(), sum(), sorted()

fruits = ["apple", "banana", "cherry", "orange"]
fruits.append("orange")
print(fruits[1:3])

#3. Dictionaries
person = {"name": "Asha", "age": 30}
person["city"] = "Bangalore"
print(person["name"])

# 4. Sets
a = {1, 2, 3}
b = {2, 3, 4}
print(a.union(b))        # {1, 2, 3, 4}
print(a.intersection(b)) # {2, 3}



# ✅ 1. Functions
# 🔹 Exercise 1: Add Two Numbers
def add_numbers(a, b):
    return a + b

print(add_numbers(5, 7))  # Output: 12

# 🔹 Exercise 2: Factorial of a Number
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(factorial(5))  # Output: 120


# ✅ 2. Lists
# 🔹 Exercise 1: Second Largest Number in a List

def second_largest(nums):
    unique_nums = list(set(nums))  # remove duplicates
    unique_nums.sort()
    return unique_nums[-2]

print(second_largest([10, 20, 4, 45, 99, 45]))  # Output: 45



# 🔹 Exercise 2: Celsius to Fahrenheit

celsius = [0, 20, 37, 100]
fahrenheit = [((9/5)*temp + 32) for temp in celsius]
print(fahrenheit)  # Output: [32.0, 68.0, 98.6, 212.0]



# ✅ 3. Dictionaries
# 🔹 Exercise 1: Student Marks Average
students = {
    "Asha": 85,
    "Ravi": 92,
    "Maya": 78
}

average = sum(students.values()) / len(students)
print(f"Average Marks: {average}")  # Output: 85.0


# 🔹 Exercise 2: Character Frequency Counter

def char_frequency(text):
    freq = {}
    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

print(char_frequency("hello world"))
# Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}


# ✅ 4. Sets
# 🔹 Exercise 1: Remove Duplicates from a List

nums = [1, 2, 2, 3, 4, 4, 5]
unique_nums = list(set(nums))
print(unique_nums)  # Output: [1, 2, 3, 4, 5]

# 🔹 Exercise 2: Common Elements in Two Lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = list(set(list1) & set(list2))
print(common)  # Output: [3, 4]