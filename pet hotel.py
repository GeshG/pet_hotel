
import random
from typing import Counter

class Hotel:

    unlucky_rooms = [3, 5, 7, 9, 11]

    def __init__(self, booked_rooms, available_rooms):
        self.booked_rooms = booked_rooms
        self.available_rooms = available_rooms
        
    def __repr__(self):
        return '{} {}'.format(self.booked_rooms, self.available_rooms)

    def book_room(self, new_client:str):
        total_available = self.available_rooms - self.booked_rooms
        if total_available <= 0:
            print('\nThere is no available rooms at the moment')
        else:
            print(f'\nWe have {total_available} rooms available.')
            client_room = random.randrange(1, total_available)
            if client_room in self.unlucky_rooms:
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
                if self.procedures[input_spa]['price'] > self.budget and self.procedures[input_spa]['time'] < self.time:
                    print(f"You need ${self.budget - self.procedures[input_spa]['price']} more for this service.")
                elif self.procedures[input_spa]['price'] < self.budget and self.procedures[input_spa]['time'] > self.time:
                    print('You don\'t have enough time')
                elif self.procedures[input_spa]['price'] > self.budget and self.procedures[input_spa]['time'] > self.time:
                    print('You don\'t have enough time and money')
                else:
                    self.budget -= self.procedures[input_spa]['price']
                    self.time -= self.procedures[input_spa]['time']
                    print(f"You will have {abs(self.time - self.procedures[input_spa]['time'])} time left")


class Restaurant:
    menu = { 
        1: {
            'starters': 'Chicken',
            'price': 70
        },
        2: {
            'starters': 'Roasted Stuffed Mushrooms',
            'price': 100,
        },
        3: {
            'starters': 'Chocolate Mousse',
            'price': 150,
        }
    }
    

    def __init__(self, budget):
        self.budget = budget
        

    def menu_order(self):
            print("="*20)
            input_menu = input('Would you like to order now? ')
            print('='*20)
            if input_menu == 'yes':
                print('Starters: ')
                select_items = []
                for item in self.menu.keys():
                    print('{}:{}'.format(item, self.menu[item]['starters']))
                while True:
                    input_choice = input('Choose from the menu above or type "stop" to end the order: ')
                    if input_choice == 'stop':
                        break
                    if input_choice.isnumeric():
                        input_choice = int(input_choice)
                        select_items.append(input_choice)

                    else:
                        print('Invalid option, please, choose from the menu or end the order')
                    
                total_items_price = 0
                selected_items_c = Counter(select_items)
                print('All products you ordered are: ')
                for item in selected_items_c.keys():
                    print(f"{self.menu[item]['starters']} x {self.menu[item]['price']}$")
                    total_items_price += self.menu[item]['price']
                if total_items_price > self.budget:
                    print('Price of the order exceeds your budget')
                else:
                    print(f"Total price of product is ${total_items_price}. Thank you for ordering")
                    self.budget -= total_items_price
                    print(f'You\'re left with ${self.budget}.')
            else:
                print('We\'ll come back')

class Pool:
    
    pools = {
        1: {
            'name': 'Professional Pool',
            'capacity': 300
        },
        2: {
            'name': 'Medium Pool',
            'capacity': 180
        },
        3: {
            'name': 'Kids Pool',
            'capacity': 70
        }
    }


    def __init__(self):
        self.pool_select = 0
        
    def pool_visit(self):
            for item in self.pools.keys():
                print('{}:{}'.format(item, self.pools[item]['name']))
                
            select_pool = int(input('Select a pool: '))
            if select_pool in self.pools.keys():
                pool_capacity = self.pools[select_pool]['capacity']
                print(f"The capacity of the pool is {pool_capacity} people")
            else:
                print('Invalid option, please, choose from the menu or end the order')

class HotelTransilvaniya:
    @classmethod
    def run(cls):
        print('WELCOME TO THE PET HOTEL')
        instructions = print(""" 
            Type 'stay' to stay in the hotel,
            Type  'spa' to use our spa center,
            Type  'menu' to use our restaurant,
            Type  'pool' to go around the center,
            Type  'checkout' to leave the center,
            """)
        active = True
        hotel1 = Hotel(100, 120)
        spa1 = Spa(60, 60)
        pool1 = Pool()
        rest1 = Restaurant(1000)
        while active:
                selection = input("What would you like to do: 'stay', 'spa', 'menu', 'pool' or 'checkout': ") 
                if selection == 'stay':
                    hotel1.book_room('Your')
                elif selection == 'spa':
                    spa1.select_procedure()
                elif selection == 'menu':
                    rest1.menu_order()
                elif selection == 'pool':
                    pool1.pool_visit()
                elif selection == 'checkout' or selection == 'check':
                    print('Thanks for passing by. Have a good one!')
                    break
                else:
                    print('Wrong selection. Please, try again')

HotelTransilvaniya.run()