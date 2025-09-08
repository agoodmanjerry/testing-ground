#!/bin/python


def get_input():
    num_1 = input("Please input the first number:")
    num_2 = input("Please input the second number:")
    return num_1, num_2


def show_op_option():
    print("1: +")
    print("2: -")
    print("3: *")
    print("4: /")


def get_operation():
    show_op_option()
    check = False
    while not check:
        op = input(
            "Which operation do you want to proceed? Please enter a number from 1 ~ 4:\n"
        )
        try:
            op_num = int(op)
            for i in range(1, 5, 1):
                if i == op_num:
                    check = True

            if check:
                return op_num
        except ValueError:
            print("Your input includes characters which are not numbers.")
            continue


def op_decode(op_code):
    op_strs = ["+", "-", "*", "/"]
    op_str = op_strs[op_code - 1]
    return op_str


def operation(num_1, num_2, op_code):
    num_1, num_2 = float(num_1), float(num_2)
    if op_code == 1:
        return num_1 + num_2
    elif op_code == 2:
        return num_1 - num_2
    elif op_code == 3:
        return num_1 * num_2
    elif op_code == 4:
        return num_1 / num_2


def main():
    print("Hello! Welcome to use simple calculator.")
    while True:
        num_1, num_2 = get_input()
        op_code = get_operation()
        op_str = op_decode(op_code)
        print(f"First number: {num_1}, Second number: {num_2}, operation: {op_str}")
        answer = operation(num_1, num_2, op_code)
        print(f"Calculation results: {answer}/n")


if __name__ == "__main__":
    main()
