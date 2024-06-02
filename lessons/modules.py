# Modules are basically a file with oython code and is used
# to organize code into multiple files like the different sections
# in a supermarket

import converters
from converters import kg_to_lbs
from utils import find_max
print(converters.kg_to_lbs(70))
print(kg_to_lbs(100))

find_max([1,3,4,2,5,3,2,6,7,3,0])