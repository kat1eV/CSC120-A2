class Computer:


   # What attributes will it need? (Define all variables and types)
   description: str
   processor_type: str
   hard_drive_capacity: int    
   memory: int
   operating_system: str
   year_made: int
   price: int


#constructor  --> where variables are defined
   def __init__(self, description: str, processor_type:str, hard_drive_capacity: int, memory: int, operating_system: str, year_made: int, price: int):
       self.description = description
       self.processor_type = processor_type
       self.hard_drive_capacity = hard_drive_capacity
       self.memory = memory
       self.operating_system = operating_system
       self.year_made = year_made
       self.price = price


#display the attributes
   def print_details(self):
       print (self.decription)
       print(self.processor_type)
       print(self.hard_drive_capacity)
       print(self.memory)
       print(self.operating_system) 
       print(self.year_made)
       print(self.price)


#Procedural version:
   #  def create_computer(self):
   #     return {'description': self.description,
   #         'processor_type': self.processor_type,
   #         'hard_drive_capacity': self.hard_drive_capacity,
   #         'memory': self.memory,
   #         'operating_system': self.operating_system,
   #         'year_made': self.year_made,
   #         'price': self.price
   #         }
    #highlight, command backslash comments out all
   # What methods will you need?
