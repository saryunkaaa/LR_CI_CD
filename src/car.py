# calculator.py

class Calculator:
    """Простой калькулятор"""
    
    def add(self, a: float, b: float) -> float:
        """Сложение"""
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        """Вычитание"""
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        """Умножение"""
        return a * b
    
    def divide(self, a: float, b: float) -> float:
        """Деление"""
        if b == 0:
            raise ValueError("Деление на ноль невозможно")
        return a / b
    
    def power(self, a: float, exponent: float) -> float:
        """Возведение в степень"""
        return a ** exponent
