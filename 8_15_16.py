# Ex 8_15 and 8_16

import sandwich
sandwich.make_sandwich('white', 'tuna', 'salad', 'tomato')

from sandwich import make_sandwich
make_sandwich('grey', 'chicken', 'mozzarella', 'zukkini')

from sandwich import make_sandwich as ms 
ms('whole grain', 'turkey', 'cheddar', 'cucumber')

import sandwich as s
s.make_sandwich('multiple grain', 'ham', 'califlour')

from sandwich import *
make_sandwich('gluten free', 'vegetables', 'cheese')