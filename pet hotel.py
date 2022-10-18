from itertools import count


class Hotel:
    def __init__(self, booked_rooms, available_rooms):
        self.booked_rooms = booked_rooms
        self.available_rooms = available_rooms
        
    def __repr__(self):
        return '{} {}'.format(self.booked_rooms, self.available_rooms)

    def book_room(self, new_client:str):
        unlucky_rooms = [3, 5, 7, 9, 11]
        total_available = self.available_rooms - self.booked_rooms
        if self.booked_rooms == self.available_rooms:
            print('\nThere is no available rooms at the moment')
        else:
            print(f'\nWe have {total_available} rooms available.')
            if total_available % 3 == 0:
                if total_available in unlucky_rooms:
                    print(f'{new_client} will look for another place.')
            else:
                print(f'{new_client} room will be number {total_available}.\n')
        

class Spa:

    budget = 100

    def __init__(self, time, price):
        self.time = time
        self.price = price
        self.procedures = {
            1:'Salt crub',
            2:'Deep tissue massage',
            3:'Holistic full body massage'
        }

    def select_procedure(self):
        [print(item) for item in self.procedures.items()]
        input_spa = input('Please, select an item: ')
        if input_spa == 1 or 2 or 3:
            if self.budget < self.price:
                print(f'You need ${abs(self.budget - self.price)} more for this service.')
            elif self.budget > self.price:
                print(f'You will have ${abs(self.budget - self.price)} left after this service.')
            else:
                print('Rethinking taking any service')


class Restaurant:
    def __init__(self):
        self.order = []
    
    def new_order(self, order):
        self.order.append(order)

    def menu_order(self):
        self.menu_prices = 0
        if not self.order:
            print('Your menu is empty')
            print("="*20)
            input_menu = input('Would you like to order now? ')
            print('='*20)
            if input_menu == 'Yes'.lower():
                menu = {
                    '1: Chicken, Salad, Dessert': 50,
                    '2: Beef, Mashed Potatoes, Dessert': 70,
                    '3: Sea Food, Sticks, Dessert': 100
                }
                print('Please, select from the following menu items: ')
                [print(item) for item in menu.items()]
                menu_selection = input(" ")
                add_to_menu = []
                #iterate through the dict and then get the key assigned to name and the value to price.
                #calculate the total amount
                for obj in menu:
                    if menu_selection == '1' or 'Chicken'.lower():
                            add_to_menu.append(obj)
                    elif menu_selection == '2' or 'Beef'.lower():
                            add_to_menu.append(obj)
                    elif menu_selection == '3' or 'Sea' or 'Sea Food':
                            add_to_menu.append(obj)
                print(add_to_menu)
            else:
                print('We\'ll come back later')
                  

class Pool:
    def __init__(self):
        self.pools = {
            '1: Professional Pool': 60,
            '2: Medium Pool': 40,
            '3: Kids Pool': 20
        }
 
    #iterate through the dict and then get the key assigned to name and the value to price.
    #calculate the total amount 
    def pool_visit(self):
        if not self.pools:
            print('You have not selected a pool')
        else:
            for item in self.pools:
                print(item)
            [print(item) for item in self.pools.items()]
            select_pool = input('Select a pool: ')
            if select_pool == '1':
                print('Hello')
            elif select_pool == '2':
                print('Bye')
            elif select_pool == '3':
                print('Dudu')


class Hotel_Transilvaniya:
    @classmethod
    def run(cls):
        print('WELCOME TO THE PET HOTEL')
        instructions = print(""" 
            Type 'stay' to stay in the hotel,
            Type  'spa' to use our spa center,
            Type  'menu' to use our restaurant,
            Type  'tour' to go around the center,
            Type  'checkout' to leave the center,
            """)
        active = True
        while active:
                selection = input("What would you like to do: 'stay', 'spa', 'menu', 'tour', 'checkout': ") 
                if selection == 'stay':
                    hotel1 = Hotel(100, 120)
                    hotel1.book_room('Your')
                elif selection == 'spa':
                    spa1 = Spa(60, 60)
                    spa1.select_procedure()
                elif selection == 'menu':
                    rest1 = Restaurant()
                    rest1.menu_order()
                elif selection == 'tour':
                    pass
                elif selection == 'checkout' or 'check':
                    print('Thanks for passing by. Have a good one!')
                    active = False
                    break

Hotel_Transilvaniya.run()