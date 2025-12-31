"""
Command-line interface for the calculator module.

Provides a CLI to perform basic arithmetic operations.
"""
import argparse
import sys
import calculator

def main():
    """
    Parses command-line arguments and performs the requested calculation.
    """
    parser = argparse.ArgumentParser(
        description="A simple command-line calculator.",
        epilog="Example: python calc_cli.py add 5 3"
    )
    parser.add_argument(
        "operation",
        choices=["add", "subtract", "multiply", "divide", "power"],
        help="The operation to perform: add, subtract, multiply, divide, power."
    )
    parser.add_argument(
        "numbers",
        nargs=2,
        type=float,
        help="The two numbers to operate on (base and exponent for power)."
    )

    args = parser.parse_args()

    operation = args.operation
    num1 = args.numbers[0]
    num2 = args.numbers[1]

    # Map operation string to the actual function
    op_map = {
        "add": calculator.add,
        "subtract": calculator.subtract,
        "multiply": calculator.multiply,
        "divide": calculator.divide,
        "power": calculator.power,
    }

    try:
        # Retrieve the function from the map and execute it
        calc_function = op_map[operation]
        result = calc_function(num1, num2)
        
        # Python's ** operator returns an int if the result is a whole number.
        # Let's ensure integer results are printed without a decimal.
        if isinstance(result, float) and result.is_integer():
            result = int(result)
            
        print(f"Result: {result}")
        
    except (ValueError, TypeError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
