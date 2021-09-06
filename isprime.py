def isPrimeNumber(number):
    if type(number) is not int:
        raise ValueError("Given Number is Not Number")
    if number<=1:
        return str(number)+" is not a prime number"
    for i in range(2, int(number/2)+1):
        if (number % i) == 0:
            return str(number)+" is not a prime number"
            break
    else:
        return str(number)+ " is a prime number"
