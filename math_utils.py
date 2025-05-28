class Calculator:
    # Метод додавання
    def add(self, a, b):
        return a + b

    # Метод віднімання
    def subtract(self, a, b):
        return a - b

    # Метод множення
    def multiply(self, a, b):
        return a * b

    # Метод ділення з перевіркою на ділення на нуль
    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b
