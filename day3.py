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


