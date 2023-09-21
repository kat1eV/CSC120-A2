#imports
from computer import*
from typing import Dict, Union, Optional


#Resale Shop Class
class ResaleShop:


    # Attributes;
    inventory : Dict[int, Dict[str, Union[str, int, bool]]] = {}


    itemID = 0 # We'll increment this every time we add a new item so that we always have a new value for the itemID
              


    # Constructor;
    def __init__(self, inventory, itemID):
        self.inventory = inventory
        self.itemID = itemID

 
#buy function---------------------------------------------------------------------


    def buyComputer(self, description: str, processor_type: str, hard_drive_capacity: int, memory: int, operating_system: str, year_made: int, price: int):
        self.itemID += 1 # increment itemID
        self.inventory[self.itemID] = self.computer
        c = Computer(description, processor_type, hard_drive_capacity, memory, operating_system,year_made, price ) 
        self.inventory.append(c) #adds computer to inventory
        print("Your newly bought " + c + " has been added to your resale shop inventory!")



#update price function-------------------------------------------------------------


    def update_price(self, new_price: int): 
        if self.item_id in self.inventory:
            self.inventory[self.item_id]["price"] = new_price
        else:
            print("Item", self.item_id, "not found. Cannot update price.")




#sell function---------------------------------------------------------------------


    def sell(self, c, inventory):
        if self.c in self.inventory:   #if the computer is actually in the inventory....
            self.inventory.remove(c)   #it is sold by removing computer "c" from inventory
            print("Item", self.item_id, "sold!")
        else:                                    #if you try to sell but have nothing left in inventory
            print("Item", self.item_id, "not found. Please select another item to sell.") 




#print inventory function---------------------------------------------------------


    def print_inventory(self, inventory): # If the inventory is not empty
        if self.inventory:
            for self.item_id in self.inventory:   # For each item
            # Print its details
                print(f'Item ID: {self.item_id} : {self.inventory[self.item_id]}') #prints attributes of computer
        else:
            print("No inventory to display.") 



#refurbish function-------------------------------------------------------------------------------------------------------


def refurbish(self, newOS, c, inventory, operating_system):
    if c in self.inventory:             #checking the computer's age and price before refurbishing
        if c == inventory.index(c):
            if c.year_made < 2000:
             c.price = 0            #if the computer dates older than 2000, then it cant be sold for money
            elif c.year_made < 2015: 
                c.price = 200       #if the computer predates 2015, but not 2000 then it can be bought for a cheap price 
            elif c.year_made < 2020:
                c.price = 500      #if the computer predates 2020, but not 2015, it can be sold for a reasonable price
            else:
                c.price = 1000      #if the computer was made after 2020, it can be sold for a more expensive price
        
        if c.price < 1000:
            c.operating_system = newOS  #if the computer is older than 2020, it should be refurbished (update the OS)
            c.price = 550                #updates price of newly refurbished computer for a reasonable price
            print("refurbishing of " + c + " has been completed! It can now be sold for " + c.price)