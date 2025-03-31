#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def main():
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a, operator, b = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print("Both operands must be integers.")
        sys.exit(1)

    operations = {'+': add, '-': sub, '*': mul, '/': div}

    if operator not in operations:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    result = operations[operator](a, b)
    print(f"{a} {operator} {b} = {result}")


if __name__ == "__main__":
    main()
