class Car:
    """Класс, представляющий автомобиль с топливным баком."""

    def __init__(self, model: str, fuel_capacity: float) -> None:
        """
        Инициализирует автомобиль.

        Args:
            model: Модель автомобиля
            fuel_capacity: Максимальная вместимость бака в литрах

        """
        self._model = model
        self._max_fuel_capacity: float = fuel_capacity
        self._fuel_in_tank: float = 0.0

    def get_current_fuel_level(self) -> float:
        """Возвращает текущий уровень топлива в баке."""
        return self._fuel_in_tank

    def refuel_car(self, fuel_quantity: float) -> None:
        """Заправить автомобиль."""
        if fuel_quantity <= 0:
            msg = "Количество топлива должно быть положительным"
            raise ValueError(msg)

        if self._fuel_in_tank + fuel_quantity > self._max_fuel_capacity:
            available = self._max_fuel_capacity - self._fuel_in_tank
            msg = f"Переполнение бака! Максимум можно долить: {available:.2f} лkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk"
            raise ValueError(msg)

        self._fuel_in_tank += fuel_quantity

    def drive(self, distance_km: float) -> float:
        """Проехать указанное расстояние в километрах."""
        if distance_km < 0:
            msg = "Расстояние должно быть неотрицательным"
            raise ValueError(msg)

        fuel_consumption_per_km = 8.0 / 100.0
        fuel_needed = fuel_consumption_per_km * distance_km

        if self._fuel_in_tank < fuel_needed - 1e-10:
            msg = f"Недостаточно топлива! Нужно {fuel_needed:.2f} л, "
            msg += f"а в баке {self._fuel_in_tank:.2f} л"
            raise ValueError(msg)

        self._fuel_in_tank -= fuel_needed
        return self.get_current_fuel_level()
