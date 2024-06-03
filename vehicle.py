class Vehicle:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self. color = color

        def move (self):
            print(f"start movin")

        def hoot (self):
            print(f"Honk Honk")

class Bus (Vehicle):
    def __init__(self, make, model, color, capacity):
        super().__init__(make,mode,)
      
        self.capacity = capacity
    def star_boarding(self):
            print(f"The bus is now boarding")


class Lorry (Vehicle):
    def __init__(self, make, model, color, max_bed):
        super().__init__(make,model,color)
        self.max_bed= max_bed
    def load(self):
            print(f"started boarding")



   
