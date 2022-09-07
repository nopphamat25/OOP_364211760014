class Vehicle:
    #class attribute
    my_vihecle = []

    def __init__(self,brand,model,color,maxspeed,price):
        self.brand = brand
        self.model =model
        self.color =color
        self.maxspeed =maxspeed
        self.price =price
        self.my_vihecle.append(self)
    def vehicle_detail (self):
        print(f'Brand:{self.brand}'
              f'Model:{self.model}'
              f'Color:{self.color}'
              f'maxspeed:{self.maxspeed}'
              f'Price:{self.price}')

