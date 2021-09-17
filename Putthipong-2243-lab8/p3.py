'''
Putthipong Phukhansung
633040224-3
Problem 3
'''


class Pet:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print(f"I'm {self.name}")

    def move(self):
        print(f"moving ...")


class Cat(Pet):
    def __init__(self, name, owner, color):
        self.owner = owner
        self.color = color
        super().__init__(name)

    def show_show(self):
        print(f"I'm {self.name} \nand is {self.color} \nbelonging to {self.owner}")

    def move(self):
        print(f"Cat likes to walk more than run")


class Dog(Pet):
    def __init__(self, name, owner, color):
        self.owner = owner
        self.color = color
        super().__init__(name)

    def show_info(self):
        print(f"I'm {self.name} \nand is {self.color} \nbelonging to {self.owner}")

    def move(self):
        print(f"Dog likes to run more than walk")

    def eat_cat(self, cat):
        print(f"Dog {self.name} eats cat {cat.name}")


if __name__ == '__main__':
    pet1 = Pet("Thongdaeng")
    pet1.show_info()
    pet1.move()
    cat1 = Cat("Thongdee", "Manee", "white");
    cat1.show_info();
    cat1.move();
    dog1 = Dog("Thongdum", "Mana", "black");
    dog1.show_info();
    dog1.move();
    dog1.eat_cat(cat1)