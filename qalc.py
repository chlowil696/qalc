"""
Qalc - A swift and simple calculate made with Python and Qt
by Chloe Wilson
"""

import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow


class Calculate:
    """Methods relating to parsing standard PEMDAS equations"""

    @staticmethod
    def generate_ast(equation: str) -> list:
        """
        Generates an abstract syntax tree with an input equation string

        :param equation: Input PEMDAS equation string
        :type equation: str
        :return: AST array
        :rtype: list[Any]
        """
        VALID_OPERATORS = ["^", "*", "/", "+", "-"]
        ast = []
        number_buffer = []
        subequation = False
        subequation_buffer = ""

        # Remove spaces from input equation string
        equation = equation.replace(" ", "")
        equation = equation.replace("×", "*")
        equation = equation.replace("÷", "/")

        # Loop through each symbol/character and the list
        for symbol in equation:
            if symbol == "(":
                subequation = True
                continue

            if symbol == ")":
                subequation = False
                subequation_object = {"obj": "seq", "val": subequation_buffer}
                ast.append(subequation_object)
                continue

            if subequation:
                subequation_buffer += symbol
                continue

            if symbol.isdigit() or symbol == ".":
                number_buffer.append(symbol)
            else:
                # Append number to AST
                if number_buffer:
                    parsed_number = "".join(number_buffer)
                    ast_object = {"obj": "num", "val": float(parsed_number)}
                    ast.append(ast_object)
                    number_buffer = []

                # Append operator to AST if valid operator is found
                if symbol in VALID_OPERATORS:
                    operator_object = {"obj": "op", "val": symbol}
                    ast.append(operator_object)
                else:
                    raise ValueError

        # Flush any remaining numbers in the buffer
        if number_buffer:
            ast_object = "".join(number_buffer)
            number_object = {"obj": "num", "val": float(ast_object)}
            ast.append(number_object)

        return ast

    @staticmethod
    def has_decimal(number: float) -> bool:
        """
        Checks whether a float is an actual decimal number
        Example:
            64.0 -> False
            3.1459 -> True

        :param number: Input floating point number to check
        :type number: float
        :return: True or False
        :rtype: bool
        """

        # Is decimal number, Ex: 3.1459
        if number % 1 != 0:
            return True

        # Not a decimal number, Ex: 64.0
        return False

    @staticmethod
    def apply_operator(left: float, right: float, operator: str) -> float:
        """
        Applies math operation to left and right numbers with given operator

        :param left: Left number
        :type left: float
        :param right: Right number
        :type right: float
        :param operator: Operator to use
        :type operator: str
        :return: Evaluated number
        :rtype: float
        """
        match operator:
            case "^":
                return float(left ** right)
            case "*":
                return float(left * right)
            case "/":
                return float(left / right)
            case "+":
                return float(left + right)
            case "-":
                return float(left - right)
        return 0.0

    @staticmethod
    def eval_pass(ast: list, operators: list) -> list:
        index = 0
        while index < len(ast):
            node = ast[index]

            # Check for sub-equations before anything else
            if node["obj"] == "seq":
                eval_number = float(Calculate.solve(node["val"]))
                ast[index] = {"obj": "num", "val": eval_number}
                index -= 1
                continue

            # Check for valid operator in equation
            if node["obj"] == "op" and node["val"] in operators:
                left = ast[index - 1]
                right = ast[index + 1]
                operator = ast[index]
                eval_number = Calculate.apply_operator(
                    left["val"], right["val"], operator["val"]
                )

                # Remove old numbers and operators from AST
                del ast[index - 1 : index + 2]
                ast.insert(index - 1, {"obj": "num", "val": eval_number})
                index -= 1
            else:
                index += 1
        return ast

    @staticmethod
    def solve(equation: str) -> str:
        """
        Solves PEMDAS equation from provided equation

        :param equation: Equation to solve
        :type equation: str
        :return: Evaluated value from equation
        :rtype: str
        """

        try:
            ast = Calculate.generate_ast(equation)
        except ValueError:
            return "Error"

        try:
            ast = Calculate.eval_pass(ast, ["^"])
            ast = Calculate.eval_pass(ast, ["*", "/"])
            ast = Calculate.eval_pass(ast, ["+", "-"])
        except (ZeroDivisionError, TypeError, OverflowError):
            return "Error"

        answer = ast[0]["val"]
        if Calculate.has_decimal(answer):
            return str(answer)
        else:
            return str(int(answer))


class Qalc(QMainWindow):
    def __init__(self, equation=""):
        """
        Main UI Process

        :param equation: Equation to solve
        """
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.equation = equation

        self.connect_widgets()

    def connect_widgets(self):
        """Connects widgets in UI to associated functions"""
        # Define number buttons to iterate through
        numbers = {
            "zero": 0,
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
        }

        # Bind functions to all numbers in numbers dictionary
        for name, number in numbers.items():
            button = getattr(self.ui, name)
            button.clicked.connect(
                lambda checked=False, n=number: self.add_number(n)
            )

        # Define operator buttons to iterate through
        operators = {
            "add": "+",
            "subtract": "-",
            "multiply": "×",
            "divide": "÷",
            "exponent": "^",
            "decimal": ".",
            "left_para": "(",
            "right_para": ")",
        }

        # Binds functions to all operators in operator dictionary
        for name, operator in operators.items():
            button = getattr(self.ui, name)
            button.clicked.connect(
                lambda checked=False, o=operator: self.add_operator(o)
            )

        # Connects other widgets
        solve_button = getattr(self.ui, "equals")
        solve_button.clicked.connect(self.equation_solve)
        clear_button = getattr(self.ui, "clear")
        clear_button.clicked.connect(self.clear_equation)
        self.ui.equation_edit.textEdited.connect(self.equation_from_edit)

    def add_number(self, number: int) -> None:
        """
        Adds a number to equation

        :param number: Number to add
        """
        self.try_clear_error()
        self.equation = self.equation + str(number)
        self.ui.equation_edit.setText(self.equation)

    def add_operator(self, operator: str) -> None:
        """
        Adds a operator to equation

        :param operator: Operator to add
        """
        self.try_clear_error()
        self.equation = self.equation + operator
        self.ui.equation_edit.setText(self.equation)

    def equation_solve(self) -> None:
        """Solves equation with user input and shows output on line edit"""
        answer = Calculate.solve(self.equation)
        self.equation = answer
        self.ui.equation_edit.setText(answer)

    def equation_from_edit(self, text: str) -> None:
        """
        Sets current equation to user inputted text from line edit widget

        :param text: Text to set as equation
        :type text: str
        """
        self.equation = text

    def try_clear_error(self) -> None:
        """Clears error text from equation if needed"""
        if self.equation == "Error":
            self.equation = ""

    def clear_equation(self) -> None:
        """Clears user inputted equation"""
        self.equation = ""
        self.ui.equation_edit.setText("0")


if __name__ == "__main__":
    app = QApplication()
    window = Qalc()
    window.show()

    sys.exit(app.exec())
