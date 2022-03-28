FIZZ = "Fizz"

def fizzbuzz(num):
    if num % 3 != 0 and num % 5 != 0: return str(num)

    retVal = ""
    if num % 3 == 0:
        retVal += FIZZ

    if num % 5 == 0:
        retVal += "Buzz"

    return retVal