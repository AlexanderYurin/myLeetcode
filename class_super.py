class Animal:
    def sing(self):
        print("Мяу")
        return "Мяу"


class Cat(Animal):
    a_1 = 0

    def sing(self):
        print("Киc")
        return super().sing()


class Dog(Cat):
    a_1 = 1

    def sing(self):
        print("РРР")
        return super().sing()

    def __getattr__(self, item):
        print(1)

    def __getattribute__(self, item):
        return self.item


a = Dog()
print(a.sing())
