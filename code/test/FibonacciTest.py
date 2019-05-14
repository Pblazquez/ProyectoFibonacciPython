import unittest
from code.Fibonacci import Fibonacci
class FibonacciTest ():
    def setUp(self):
        self.fibonacci = Fibonacci()

    def test_should_fibonacci_number_of_months_1_and_pairs_produced_3_return_1(self):
        self.assertEqual(1, self.fibonacci.compute(1, 3))

    def shouldFibonacciNumber1Pair3Return1(self):
        self.assertEqual(1,self.fibonacci.compute(1,3))

    def  shouldFibonacciNumber2Pair3Return1(self):
        self.assertEquals(1, self.fibonacci.compute(2,3))

    def shouldFibonacciNumber3Pair3Return4(self):
        self.assertEqual(4, self.fibonacci.compute(3, 3))

    def shouldFibonacciNumber4Pair3Return7(self):
        self.assertEqual(7, self.fibonacci.compute(4, 3))

    def shouldFibonacciNumber5Pair3Return19(self):
        self.assertEqual(19, self.fibonacci.compute(5, 3))

    def shouldFibonacciNumber6Pair3Return40(self):
        self.assertEqual(40, self.fibonacci.compute(6, 3))

    def shouldFibonacciNumber7Pair3Return97(self):
        self.assertEqual(97, self.fibonacci.compute(7, 3))

if __name__ == '__main__':
    unittest.main()
