
import random

class Hotel:
    def __init__(self, booked_rooms, available_rooms):
        self.booked_rooms = booked_rooms
        self.available_rooms = available_rooms
        
    def __repr__(self):
        return '{} {}'.format(self.booked_rooms, self.available_rooms)

    def book_room(self, new_client:str):
        unlucky_rooms = [3, 5, 7, 9, 11]
        total_available = self.available_rooms - self.booked_rooms
        if total_available <= 0:
            print('\nThere is no available rooms at the moment')
        else:
            print(f'\nWe have {total_available} rooms available.')
            client_room = random.randrange(1, total_available)
            if client_room in unlucky_rooms:
                print(f'{new_client} will look for another place.')
            else:
                print(f'{new_client} room will be number {client_room}.\n')
                self.available_rooms -= 1
        

class Spa:

    budget = 100
    procedures = {
        1:{
            'name': 'Salt crub',
            'price': 50,
            'time': 40
        },
        2: {
            'name': 'Deep tissue massage',
            'price': 40,
            'time': 30
        },
        3: {
            'name': 'Holistic full body massage',
            'price': 40,
            'time': 30
        }
    }

    def __init__(self, time, price):
        self.time = time
        self.price = price
       

    def select_procedure(self):
        for item_num in self.procedures.keys():
            print("{}:{}".format(item_num, self.procedures[item_num]['name']))
        input_spa = int(input('Please, select an item: '))

        if input_spa == 1 or input_spa == 2 or input_spa == 3:
            if input_spa in self.procedures.keys():
                if self.procedures[input_spa]['price'] > self.budget:
                    print(f"You need ${self.budget - self.procedures[input_spa]['price']} more for this service.")
                else:
                    print(f"You will have ${self.budget - self.procedures[input_spa]['price']} left after this service.")
                    self.budget -= self.procedures[input_spa]['price']
                if self.procedures[input_spa]['time'] > self.time:
                        print(f"You don't have enough time")
                else:
                    self.time -= self.procedures[input_spa]['time']
                    print(f"You will have {self.time - self.procedures[input_spa]['time']} time left")


class Restaurant:
    menu = { 
        1: {
            'starters': 'Salmon Nicoise',
            'main_course':'Chicken',
            'dessert': 'Icecream',
            'price': 70
        },
        2: {
            'starters': 'Roasted Stuffed Mushrooms',
            'main_course': 'Cross Rib Roast',
            'dessert': 'Coconut yoghurt cake',
            'price': 100,
        },
        3: {
            'starters': 'Cheese Poppers',
            'main_course': 'Grilled Salmon',
            'dessert': 'Chocolate Mousse',
            'price': 150,
        }
    }
    budget = 100

    def __init__(self):
        self.order = []
    
    def new_order(self, order):
        self.order.append(order)

    def menu_order(self):
        self.menu_prices = 0
        if not self.order:
            print('Your order is empty')
            print("="*20)
            input_menu = input('Would you like to order now? ')
            print('='*20)
            if input_menu == 'Yes'.lower():
                print('Starters: ')
                select_items = []
                for item in self.menu.keys():
                    print('{}:{}'.format(item, self.menu[item]['starters']))
                menu_selection = int(input('Please, select a nunber for starter: '))
                select_items.append(menu_selection)
                print('Main Courses: ')
                for item in self.menu.keys():
                    print('{}:{}'.format(item, self.menu[item]['main_course']))
                menu_selection = int(input('Please, select a nunber for main course: '))
                select_items.append(menu_selection)
                for item in self.menu.keys():
                    print('{}:{}'.format(item, self.menu[item]['dessert']))
                menu_selection = int(input('Please, select a nunber for dessert: '))
                select_items.append(menu_selection)
                print(f'You have selected the following items: {select_items}')
                if self.budget > (f"{self.menu.keys[menu_selection]['price']}"):
                    print(sum(menu_selection['price']))
                else:
                    print('Loading.....')
            else:
                print('We\'ll come back later')
                

class Pool:
    
    pools = {
        1: {
            'name': 'Professional Pool',
            'price': 60
        },
        2: {
            'name': 'Medium Pool',
            'price': 40
        },
        3: {
            'name': 'Kids Pool',
            'price': 20
        }
    }

    budget = 100

    def __init__(self):
        self.pool_select = []

    def pool_visit(self):
        if not self.pools:
            print('You have not selected a pool')
        else:
            for item in self.pools.keys():
                print('{}:{}'.format(item, self.pools[item]['name']))
            select_pool = int(input('Select a pool: '))
            if select_pool == 1:
                if self.pools.keys([item]['price']) > self.budget:
                    print('Not enough budget')
            elif select_pool == 2:
                print('Bye')
            elif select_pool == 3:
                print('Dudu')


class HotelTransilvaniya:
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
        hotel1 = Hotel(100, 120)
        spa1 = Spa(60, 60)
        rest1 = Restaurant()
        pool1 = Pool()
        while active:
                selection = input("What would you like to do: 'stay', 'spa', 'menu', 'tour', 'checkout': ") 
                if selection == 'stay':
                    hotel1.book_room('Your')
                elif selection == 'spa':
                    spa1.select_procedure()
                elif selection == 'menu':
                    rest1.menu_order()
                elif selection == 'tour':
                    pool1.pool_visit()
                elif selection == 'checkout' or selection == 'check':
                    print('Thanks for passing by. Have a good one!')
                    break
                else:
                    print('Wrong selection. Please, try again')

HotelTransilvaniya.run()