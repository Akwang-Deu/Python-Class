class Animal:
    def make_sound(self):
        pass
    def move(self):
        pass
    def reproduction(self):
        pass


class Bird(Animal):
    def make_sound(self):
        print("chirp")
    def move(self):
        print("The bird is flying")
    def reproduction(self):
        print("The bird lay eggs")
    


class Fish(Animal):
    def make_sound(self):
        print("click")
    
    def move(self):
        print("swimming")   
    def reproduction(self):
        print("The fish lay eggs")
    


class Dog (Animal):
    def make_sound(self):
        print("Barking")
    def move(self):
        print("The dog is running")
    def reproduction(self):
        print("The dog give birth")
    

class Cat (Animal):
    def make_sound(self):
        print("Moew")
    def move(self):
        print("The cat is walking")
    def reproduction(self):
        print("The cat give birth")
    

    