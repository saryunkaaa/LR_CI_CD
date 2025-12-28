class Car:
    def __init__(self, brand: str, max_fuel: float):
        self.brand = brand
        self.max_fuel = max_fuel
        self.current_fuel = 0.0
    
    def refuel(self, amount: float):
        if amount < 0:
            raise ValueError("Количество топлива не может быть отрицательным")
        
        if self.current_fuel + amount > self.max_fuel:
            raise ValueError("Слишком много топлива")
        
        self.current_fuel += amount
    
    def drive(self, distance: float):
        fuel_per_km = 0.08  # 8 литров на 100 км
        fuel_needed = distance * fuel_per_km
        
        if fuel_needed > self.current_fuel:
            raise ValueError("Недостаточно топлива")
        
        self.current_fuel -= fuel_needed
        return f"Проехали {distance} км. Осталось топлива: {self.current_fuel:.1f} л"
    
    def get_fuel_info(self):
        return f"{self.brand}: {self.current_fuel:.1f}/{self.max_fuel} л"
