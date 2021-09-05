### TODO:
#   - code a Pants class with the following attributes
#   - color (string) eg 'red', 'yellow', 'orange'
#   - waist_size (integer) eg 8, 9, 10, 32, 33, 34
#   - length (integer) eg 27, 28, 29, 30, 31
#   - price (float) eg 9.28

### TODO: Declare the Pants Class 

### TODO: write an __init__ function to initialize the attributes

### TODO: write a change_price method:
#    Args:
#        new_price (float): the new price of the shirt
#    Returns:
#        None

### TODO: write a discount method:
#    Args:
#        discount (float): a decimal value for the discount. 
#            For example 0.05 for a 5% discount.
#
#    Returns:
#        float: the discounted price
#__init__ => special build in function/ magic method
class Pants:
    def __init__(self,pants_color,waist_size, pants_length, pants_price):
        self.color = pants_color
        self.size = waist_size
        self.length = pants_length
        self.price = pants_price

    def __str__(self):#magic method
        return f'{self.color}'

    def __len__(self):
        return self.length

    def change_price(self, new_price):
        self.price = new_price

    def discount(self, discount):
        return self.price * (1 - discount)

pant1 = Pants('red', 35, 36, 15.33)
print(str(pant1))
print(len(pant1))