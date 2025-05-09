#- [ ] Day 4: Understand OOP: classes, objects, inheritance

class Person:
    # Constructor to initialize the person's name and age
    def __init__(self, name, age):
        self.name = name  # Set the name attribute
        self.age = age  # Set the age attribute

    # Method to print a greeting message
    def greet(self):
        print(f"Name - {self.name} and Age - {self.age}.")


# Create an instance of the Person class
p1 = Person("Alice", 30)

# Call the greet method to display the greeting message
p1.greet()



fruits = [ "zzz","cherry","apple", "banana",]
fruits.append("orange")
print(sorted(fruits[1]))



person = {"name": "Asha", "age": 30,"State":"karnataka"}
person["city"] = "Bangalore"
person["State"] = "karnataka"
person["State"] = "karnataka"
print(person)


#Execise Character Frequency Counter
# {'H': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

def char_freq(text):
    freq={}
    for char in text:
        if char in freq:
            freq[char]+=1
        else:
            freq[char]=1
    return freq
print(char_freq("Hello world"))

