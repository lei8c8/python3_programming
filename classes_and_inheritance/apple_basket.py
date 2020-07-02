class AppleBasket():

    def __init__(self, apple_color, apple_quantity):
        self.apple_color = apple_color
        self.apple_quantity = apple_quantity

    def increase(self):
        self.apple_quantity += 1

    def __str__(self):
        return "A basket of {} {} apples.".format(self.apple_quantity, self.apple_color)


instance1 = AppleBasket("red", 100)
instance1.increase()
print(instance1)
       