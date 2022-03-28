import pytest
from fizzbuzz.fizzbuzz import fizzbuzz

# - Can I call FizzBuzz :check:
# - Get "1" when pass in 1 :check:
# - Get "2" when pass in 2 :check:
# - Get "Fizz" when pass in 3 :check:
# - Get "Buzz" when pass in 5 :check:
# - Get "Fizz" when pass in 6 (multiple of 3) :check:
# - Get "Buzz" when pass in 10 (multiple of 5) :check:
# - Get "FizzBuzz" when pass in 15 (multiple of 3 and 5)
# - Be able to change the strings to something new

def test_get2WhenGiven2():
    retVal = "2"
    assert fizzbuzz(2) == retVal

def test_getFizzWhenGiven6():
    retVal = "Fizz"
    assert fizzbuzz(6) == retVal

def test_getBuzzWhenGiven10():
    retVal = "Buzz"
    assert fizzbuzz(10) == retVal

def test_getFizzBuzzWhenGiven15():
    retVal = "FizzBuzz"
    assert fizzbuzz(15) == retVal