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
        self.title("Maangas Simple Calculator 3000")
        self.geometry("400x550")
        ctk.set_appearance_mode("dark")
        
        self.operations = {
            "Addition": Addition(), "Subtraction": Subtraction(),
            "Multiplication": Multiplication(), "Division": Division()
        }
        self.setup_ui()

    def setup_ui(self):
        ctk.CTkLabel(self, text="CALCULATOR 3000", font=("Impact", 24, "bold"), text_color="orange").pack(pady=20)
        self.num1_entry = ctk.CTkEntry(self, placeholder_text="Enter first number", width=250)
        self.num1_entry.pack(pady=10)
        self.operation_var = ctk.StringVar(value="Addition")
        ctk.CTkOptionMenu(self, variable=self.operation_var, values=list(self.operations.keys()), width=250).pack(pady=10)
        self.num2_entry = ctk.CTkEntry(self, placeholder_text="Enter second number", width=250)
        self.num2_entry.pack(pady=10)
        self.calc_btn = ctk.CTkButton(self, text="Calculate", command=self.calculate, font=("Arial", 16, "bold"))
        self.calc_btn.pack(pady=20)
        self.result_label = ctk.CTkLabel(self, text="Result will appear here", font=("Arial", 18), text_color="yellow")
        self.result_label.pack(pady=10)

    def calculate(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            op_name = self.operation_var.get()

            operation = self.operations[op_name]
            result = operation.execute(num1, num2)

            if result.is_integer(): result = int(result)
            self.result_label.configure(text=f"Result: {result}", text_color="#00FF00")

            log_entry = f"{op_name}: {num1} and {num2} = {result}\n"
            self.history_box.configure(state="normal")
            self.history_box.insert("end", log_entry)
            self.history_box.configure(state="disabled")

        except ValueError:
            self.result_label.configure(text="Error: Letters not allowed!", text_color="#FF4444")
        except ZeroDivisionError as e:
            self.result_label.configure(text=f"Error: {e}", text_color="#FF4444")
        except Exception:
            self.result_label.configure(text="Unexpected Error!", text_color="#FF4444")

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()