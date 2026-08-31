class Fruit:
    '''Fruit Class'''

    __slots__ = ['type', 'price']

    def __init__(self, type, price):
        self.type = type
        self.price = price

def print_fruit(fruit):
    print(fruit.type, fruit.price)

def get_price_from_basket(basket):
    price = 0
    for fruit in basket:
        count = basket[fruit]
        price += basket[fruit].price * count

    return price

def get_fruit_count(basket, a_fruit):
    return basket[a_fruit]

def add_to_basket(basket, fruit):
    if fruit in basket:
        basket[fruit] += 1
    else:
        basket[fruit] = 1

def create_fruit(fruit_shop, type, price):
    fruit = Fruit(type, price)
    fruit_shop [type.lower()] = fruit

def main():
    fruit_shop = {}
    create_fruit(fruit_shop, "kiwi", 3.15)

    basket = {}
    fruit = ' '
    while fruit != '':
        fruit = input("Enter a fruit: ")
        if fruit == fruit.type.lower():
            add_to_basket(basket, fruit)
        elif fruit == fruit.type.lower():
            add_to_basket(basket, fruit)
        elif fruit != '':
            print("We don't got no", fruit)
    
    for fruit in basket:
        print_fruit(fruit)

    print("You have $", get_price_from_basket(basket), " worth of fruit.", sep='')

    print("There are", get_fruit_count(basket, "kiwi"), "kiwis in your basket.")

main()