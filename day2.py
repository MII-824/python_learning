print("Hello, world!")


 #2. Variables and Data Types
name = "Alice"      # string
height = 5.7        # float
is_student = True   # boolean
is_active = True       # bool
fruits = ["apple", "banana"]  # list
person = {"name": "Alice", "age": 25}  # dict

# Input from User
name = input("What is your name? ")
print("Hello", name)



#☐ Practice Type Checking and Casting
print(type(name))        # <class 'str'>
age = int("30")          # casting str to int
#➕ Arithmetic
a = 10
b = 3
print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.33
print(a % b)   # 1 (remainder)


# Comparison
a == b  # False
a > b   # True
a != b  # True


#🔄 Logical

True and False   # False
True or False    # True
not True         # False
# ✅ 5. Comments

# This is a single-line comment
"""
This is a 
multi-line comment
"""

# ☐ If/Else Statements
if age >= 18:
    print("Adult")
else:
    print("Minor")

# ☐ Elif(ElseIf)
temp = 30
if temp > 35:
    print("Hot")
elif temp > 20:
    print("Warm")
else:
    print("Cold")


# ☐ Loops For Loop:

for i in range(5):
    print(i)

# While Loop:

count = 0
while count < 5:
    print(count)
    count += 1