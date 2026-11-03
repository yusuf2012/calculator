"""
Calculator with history
Usage: python calculator.py
"""

class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a: float, b: float) -> float:
        result = a + b
        self._save(f"{a} + {b} = {result}")
        return result

    def subtract(self, a: float, b: float) -> float:
        result = a - b
        self._save(f"{a} - {b} = {result}")
        return result

    def multiply(self, a: float, b: float) -> float:
        result = a * b
        self._save(f"{a} × {b} = {result}")
        return result

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self._save(f"{a} ÷ {b} = {result}")
        return result

    def power(self, a: float, b: float) -> float:
        result = a ** b
        self._save(f"{a} ^ {b} = {result}")
        return result

    def _save(self, entry: str) -> None:
        self.history.append(entry)

    def show_history(self) -> None:
        if not self.history:
            print("No calculations yet.")
            return
        print("\n📜 History:")
        for i, entry in enumerate(self.history, 1):
            print(f"  {i}. {entry}")

    def clear_history(self) -> None:
        self.history.clear()
        print("🧹 History cleared.")


def main():
    calc = Calculator()
    print("🧮 Calculator (type 'history', 'clear', or 'quit')")

    while True:
        try:
            expr = input("\n> ").strip().lower()
            if expr == "quit":
                break
            elif expr == "history":
                calc.show_history()
            elif expr == "clear":
                calc.clear_history()
            else:
                result = eval(expr, {"__builtins__": {}}, {})
                print(f"= {result}")
        except ZeroDivisionError:
            print("❌ Cannot divide by zero")
        except Exception:
            print("❌ Invalid expression. Try: 10 + 5 or 3 * 4")


if __name__ == "__main__":
    main()