class TooMuchFuelError(Exception):
    pass

class NotEnoughFuelError(Exception):
    pass

class Car:
    
    def __init__(self, model: str, fuel_capacity: float) -> None:
        self.model = model
        self.max_fuel_capacity = fuel_capacity
        self.fuel_in_tank = 0
    
    def get_current_fuel_level(self) -> float:
        return self.fuel_in_tank
    
    def refuel_car(self, fuel_quantity: float):
        if fuel_quantity < 0:
            raise ValueError("Количество топлива не может быть отрицательным")
        
        if self.fuel_in_tank + fuel_quantity > self.max_fuel_capacity:
            raise TooMuchFuelError("Вы пытаетесь залить слишком много бензина!")
        
        self.fuel_in_tank += fuel_quantity
    
    def drive(self, distance_km: float):
        if distance_km < 0:
            raise ValueError("Дистанция не может быть отрицательной")
        
        fuel_consumption_per_100km = 8
        fuel_burned = fuel_consumption_per_100km * (distance_km / 100)
        
        if self.fuel_in_tank < fuel_burned:
            raise NotEnoughFuelError("Не доедем жёж...")
        
        self.fuel_in_tank -= fuel_burned
        return self.get_current_fuel_level()
