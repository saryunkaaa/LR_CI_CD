class Car:
    def __init__(self, model: str, fuel_capacity: float) -> None:
        self._model = model
        self._max_fuel_capacity: float = fuel_capacity
        self._fuel_in_tank: float = 0.0

    def get_current_fuel_level(self) -> float:
        return self._fuel_in_tank

    def refuel_car(self, fuel_quantity: float) -> None:
        """Заправить автомобиль."""
        if fuel_quantity <= 0:
            raise ValueError("Количество топлива должно быть положительным")
        
        if self._fuel_in_tank + fuel_quantity > self._max_fuel_capacity:
            raise ValueError(f"Переполнение бака! Максимум можно долить: "
                           f"{self._max_fuel_capacity - self._fuel_in_tank:.2f} л")
        
        self._fuel_in_tank += fuel_quantity

    def drive(self, distance_km: float) -> float:
        """Проехать указанное расстояние в километрах."""
        if distance_km < 0:  # Исправлено: < вместо <=
            raise ValueError("Расстояние должно быть неотрицательным")
        
        # Расход 8 литров на 100 км
        fuel_consumption_per_km = 8.0 / 100.0
        fuel_needed = fuel_consumption_per_km * distance_km
        
        # Исправляем проблему с плавающей точкой
        if self._fuel_in_tank < fuel_needed - 1e-10:
            raise ValueError(f"Недостаточно топлива! Нужно {fuel_needed:.2f} л, "
                           f"а в баке {self._fuel_in_tank:.2f} л")
        
        self._fuel_in_tank -= fuel_needed
        return self.get_current_fuel_level()
