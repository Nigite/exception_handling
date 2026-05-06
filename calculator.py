import customtkinter as ctk

class MathOperation:
    def execute(self, a, b): pass
class Addition(MathOperation):
    def execute(self, a, b): return a + b
class Subtraction(MathOperation):
    def execute(self, a, b): return a - b
class Multiplication(MathOperation):
    def execute(self, a, b): return a * b
class Division(MathOperation):
    def execute(self, a, b):
        if b == 0: raise ZeroDivisionError("Cannot divide by zero!")
        return a / b

class CalculatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Maangas Calculator 3000")
        self.geometry("400x550")
        ctk.set_appearance_mode("dark")
        
        self.operations = {
            "Addition": Addition(), "Subtraction": Subtraction(),
            "Multiplication": Multiplication(), "Division": Division()
        }