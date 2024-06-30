# main.py
from Math_Package.add import add
from Math.sub import sub
from Math.multi import multi
from math.div import div
from math.mod import mod
from math.exp import power
from math.sqrt import sqrt

def main():
    print("Addition: 5 + 3 =", add(5, 3))
    print("Subtraction: 5 - 3 =", sub(5, 3))
    print("Multiplication: 5 * 3 =", multi(5, 3))
    print("Division: 5 / 3 =", div(5, 3))
    print("Modulus: 5 % 3 =", mod(5, 3))
    print("Exponentiation: 5 ** 3 =", power(5, 3))
    print("Square Root: sqrt(25) =", sqrt(25))
    
    print(divide(5, 0))

if __name__ == "__main__":
    main()
