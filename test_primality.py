import unittest
from isprime import isPrimeNumber
class TestPrimality(unittest.TestCase):
    def test_primeOrNot(self):
        self.assertSequenceEqual(isPrimeNumber(1),"1 is not a prime number")
        self.assertEquals(isPrimeNumber(0),"0 is not a prime number")
        self.assertEquals(isPrimeNumber(4),"4 is not a prime number")
        self.assertEquals(isPrimeNumber(6),"6 is not a prime number")
        self.assertEquals(isPrimeNumber(3),"3 is a prime number")
        self.assertEquals(isPrimeNumber(5),"5 is a prime number")
        self.assertEquals(isPrimeNumber(7),"7 is a prime number")
        self.assertEquals(isPrimeNumber(11),"11 is a prime number")

    def test_checkType(self):
        self.assertRaises(ValueError,isPrimeNumber,"hai")
        self.assertRaises(ValueError,isPrimeNumber,1.9)