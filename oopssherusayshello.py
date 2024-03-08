class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says hello!"

dog = Animal("Sheru")
print(dog.speak())
