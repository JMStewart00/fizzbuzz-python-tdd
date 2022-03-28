"""
- Create Instance of House
- Set and get number of rooms
- set and get numbers of bathrooms
- Determine whether or not the house has a garage, then how many cars
- Calculate the square footage
- Determine price 
"""

import pytest
from housebuilder import House

def test_createHouse():
    h = House()
    assert isinstance(h, House)

