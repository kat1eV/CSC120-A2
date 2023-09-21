#imports
from oo_resale_shop import*  
from oo_resale_shop import ResaleShop as shop 
#computer and dictionary added just incase not exactly imported from oo_resale_shop...
from typing import Dict, Union, Optional
from computer import*  
from computer import Computer as comp

def main():

# Print a banner------------------------------------------
    print("-" * 29)
    print("Katie's Computer Resale Shop")
    print("-" * 29)


# Creating a computer and assigning it attributes
    c = Computer(
    "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )
    comp.print_details(c) 


# (Check the inventory to make sure 'buy' worked correctly)-------------------------
def checkInventory():
    print("Checking inventory...")
    shop.print_inventory()
    print ("End of inventory list.")


# Buy---------------------------------------------------- 
    print("Buying", Computer["description"])
    print("Adding to inventory...")   
    shop.buyComputer() #using the function from oo_resale_shop
    if shop.itemID >= 1:
        print(f"Computer {Computer['description']} has been successfully bought")
  

# Refurbish---------------------------------------------------
    new_OS = "MacOS Monterey"
    print ("Refurbishing "+Computer["description"]+ ". Updating OS to " +new_OS+".")
    print("Updating inventory...")
    refurbish(Computer, new_OS)
    print("Refurbish completed!")
    checkInventory()


# Sell ------------------------------------------------
    print("Selling computer " +Computer["description"]+".")
    shop.sell(Computer)
    checkInventory()


#Calls the main() function when this file is run
if __name__ == "__main__": main()