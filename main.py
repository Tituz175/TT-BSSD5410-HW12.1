a = b = 0


def inp1():
    global a
    a = int(input("Enter Num: "))


def inp2():
    global a, b
    a = int(input("Enter A: "))
    b = int(input("Enter B: "))


class Input:
    # *=42, +43,-45,/47,^94
    operators = ["+", "-", "*", "^", "**"]

    def menu(self):
        print("====Calculator====\nSelect an operator")
        for symbol in self.operators:
            print(symbol)

    def get_operator(self, ch):
        if ch == "**":
            operator_name = "inp_pow"
        else:
            if ch not in self.operators:
                return None, "Invalid Option"
            else:
                ch = ord(ch)
                operator_name = f"inp_{ch}"
        operator = getattr(self, operator_name, lambda: "Invalid Option")
        return operator(), ch

    def inp_43(self):
        inp2()

    def inp_45(self):
        inp2()

    def inp_47(self):
        inp2()

    def inp_42(self):
        inp2()

    def inp_pow(self):
        inp2()

    def inp_94(self):
        inp1()


class Calculator:
    def calculate(self, ch):
        if ch == "**":
            operator_name = f"cal_pow"
        else:
            operator_name = f"cal_{ch}"
        operator = getattr(self, operator_name, lambda: "Invalid Operator")
        return operator()

    # *=42, +43,-45,/47,^94

    def cal_43(self):
        return a + b

    def cal_45(self):
        return a - b

    def cal_42(self):
        return a * b

    def cal_47(self):
        return a / b

    def cal_94(self):
        return a * a

    def cal_pow(self):
        return a ** b


def main():
    userInput = Input()
    userInput.menu()
    operator = input("Enter Choice(+-^): ")
    _, operator = userInput.get_operator(operator)

    calculator = Calculator()
    ans = calculator.calculate(operator)
    print(f"Your answer is {ans}.")


if __name__ == "__main__":
    main()
