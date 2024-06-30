# main.py
from math_package import addition, subtraction, multiplication, division, modulus, power, sqrtroot

def main():
    print("Addition: 5 + 3 =", addition(5, 3))
    print("Subtraction: 5 - 3 =", subtraction(5, 3))
    print("Multiplication: 5 * 3 =", multiplication(5, 3))
    print("Division: 5 / 3 =", division(5, 3))
    print("Modulus: 5 % 3 =", modulus(5, 3))
    print("Exponentiation: 5 ** 3 =", power(5, 3))
    print("Square Root: sqrt(25) =", sqrtroot(25))
    
if __name__ == "__main__":
    main()
