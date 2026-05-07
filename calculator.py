import customtkinter as ctk

class MathOperation:
    def __init__(self, num1, num2):
        self._num1 = num1  
        self._num2 = num2
    def execute(self):
        pass
class Addition(MathOperation):
    def execute(self): 
        return self._num1 + self._num2
class Subtraction(MathOperation):
    def execute(self): 
        return self._num1 - self._num2
class Multiplication(MathOperation):
    def execute(self): 
        return self._num1 * self._num2
class Division(MathOperation):
    def execute(self):
        if self._num2 == 0: 
            raise ZeroDivisionError("Cannot divide by zero!")
        return self._num1 / self._num2

class CalculatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Maangas Calculator 3000")
        self.geometry("400x550")
        ctk.set_appearance_mode("dark")
        
        self.operation_classes = {
            "Addition": Addition, 
            "Subtraction": Subtraction,
            "Multiplication": Multiplication, 
            "Division": Division
        }
        self.setup_ui()

    def setup_ui(self):
        ctk.CTkLabel(self, text="CALCULATOR 3000", font=("Impact", 24, "bold"), text_color="orange").pack(pady=20)
        self.num1_entry = ctk.CTkEntry(self, placeholder_text="Enter first number", width=250)
        self.num1_entry.pack(pady=10)
        self.operation_var = ctk.StringVar(value="Addition")
        ctk.CTkOptionMenu(self, variable=self.operation_var, values=list(self.operation_classes.keys()), width=250).pack(pady=10)
        self.num2_entry = ctk.CTkEntry(self, placeholder_text="Enter second number", width=250)
        self.num2_entry.pack(pady=10)
        self.calc_btn = ctk.CTkButton(self, text="Calculate", command=self.calculate, font=("Arial", 16, "bold"))
        self.calc_btn.pack(pady=20)
        self.result_label = ctk.CTkLabel(self, text="Result will appear here", font=("Arial", 18), text_color="yellow")
        self.result_label.pack(pady=10)
        ctk.CTkLabel(self, text="Session History:", font=("Arial", 14, "bold")).pack(pady=(10, 0))
        self.history_box = ctk.CTkTextbox(self, width=300, height=100)
        self.history_box.pack(pady=5)
        self.history_box.insert("0.0", "Logs:\n")
        self.history_box.configure(state="disabled")

    def calculate(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            op_name = self.operation_var.get()
            op_class = self.operation_classes[op_name]
            operation = op_class(num1, num2) 
            result = operation.execute()
            
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