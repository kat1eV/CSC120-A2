#imports
from oo_resale_shop import*
from oo_resale_shop import buyComputer, update_price, sell, print_inventory, refurbish, itemID
from computer import*  #computer and dictionary added just incase not exactly imported from oo_resale_shop...
from typing import Dict, Union, Optional
from computer import print_details 

def main():

# Creating a computer and assigning it attributes
    c = Computer  (
    "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )


# Print a banner
    print("-" * 21)
    print("Katie's Computer Resale Shop")
    print("-" * 21)



# Buy---------------------------------------------------- 
    print("Buying", c["description"])
    print("Adding to inventory...")   
    buyComputer() #using the function from oo_resale_shop
    if itemID >= 1:
        print ("Computer "c["description"] " has been successfully bought")
    



# (Check the inventory to make sure 'buy' worked correctly)-------------------------
    print("Checking inventory...")
    print_inventory()
    print ("End of inventory list.")



# Refurbish---------------------------------------------------
    newOS = "MacOS Monterey"
    print ()



#Code from procedural resaleshop:

  # Now, let's refurbish it
    new_OS = "MacOS Monterey"
    print("Refurbishing Item ID:", computer_id, ", updating OS to", new_OS)
    print("Updating inventory...")
    refurbish(computer_id, new_OS)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    print_inventory()
    print("Done.\n")
    
    # Now, let's sell it!
    print("Selling Item ID:", computer_id)
    sell(computer_id)
    
    # Make sure it worked by checking inventory
    print("Checking inventory...")
    print_inventory()
    print("Done.\n")

# Calls the main() function when this file is run
if __name__ == "__main__": main()



