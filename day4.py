
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


