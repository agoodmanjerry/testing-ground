#!/bin/python


class calculator:
    def __init__(self):
        self.num_1 = None
        self.num_2 = None
        self.op_code = None

    def check_q(self, input_str):
        if input_str == "q":
            print("See you next time!")
            quit()

    def get_input(self, message_str):
        input_str = input(message_str)
        self.check_q(input_str)
        return input_str

    def get_input_nums(self):
        self.num_1 = self.get_input("Please input the first number:")
        self.num_2 = self.get_input("Please input the second number:")

    def show_op_option(self):
        print("1: +")
        print("2: -")
        print("3: *")
        print("4: /")

    def get_operation(self):
        check = False
        while not check:
            self.show_op_option()
            op = self.get_input(
                "Which operation do you want to proceed? Please enter a number from 1 ~ 4:\n"
            )
            try:
                op_code = int(op)
                for i in range(1, 5, 1):
                    if i == op_code:
                        check = True

                if check:
                    self.op_code = op_code
            except ValueError:
                print("Your input includes characters which are not numbers.")
                continue

    def output(self):
        if self.num_1 is not None and self.num_2 is not None:
            return float(self.num_1), float(self.num_2), self.op_code
        else:
            print("The input numbers are not assigned correctly.")

    def op_decode(self, op_code):
        op_strs = ["+", "-", "*", "/"]
        op_str = op_strs[op_code - 1]
        return op_str

    def operate(self, num_1, num_2, op_code):
        num_1, num_2 = float(num_1), float(num_2)
        op_str = self.op_decode(op_code)
        print(f"First number: {num_1}, Second number: {num_2}, operation: {op_str}")
        if op_code == 1:
            self.answer = num_1 + num_2
        elif op_code == 2:
            self.answer = num_1 - num_2
        elif op_code == 3:
            self.answer = num_1 * num_2
        elif op_code == 4:
            self.answer = num_1 / num_2
        print(f"Calculation results: {self.answer}")
        print("Press 'q' to leave.\n")
        return self.answer


def main():
    print("Hello! Welcome to use simple calculator. Press 'q' to leave.")
    cal = calculator()
    while True:
        cal.get_input_nums()
        cal.get_operation()
        num_1, num_2, op_code = cal.output()
        cal.operate(num_1, num_2, op_code)


if __name__ == "__main__":
    main()
