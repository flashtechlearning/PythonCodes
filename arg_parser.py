import argparse

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("number1" , help="first number")
    parser.add_argument("number2" , help="first number")
    parser.add_argument("operation" , help="operation")
    args = parser.parse_args()



    n1 = int(args.number1)
    n2 = int(args.number2)
    op = args.operation
    result = None

    if op == "add":
        result = n1 + n2
    elif op == "sub":
        result = n1 - n2
    elif op == "multiply":
        result = n1 * n2
    else:
        print("Wrong Operation")

    print(args.number1)
    print(args.number2)
    print("Result:" , result)


if __name__ == '__main__':
    main()
