import unittest
from car import Car


class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car(model="BMW X5", fuel_capacity=80.0)

    def test_initial_state(self):
        """Тест начального состояния автомобиля."""
        self.assertEqual(self.car.get_current_fuel_level(), 0.0)

    def test_refuel_valid(self):
        """Тест корректной заправки."""
        self.car.refuel_car(20.0)
        self.assertAlmostEqual(self.car.get_current_fuel_level(), 20.0, places=2)
        
        # Доливаем ещё
        self.car.refuel_car(30.0)
        self.assertAlmostEqual(self.car.get_current_fuel_level(), 50.0, places=2)

    def test_refuel_overflow(self):
        """Тест переполнения бака."""
        # Пытаемся залить больше, чем вмещается
        with self.assertRaises(ValueError) as context:
            self.car.refuel_car(90.0)
        self.assertIn("Переполнение", str(context.exception))

    def test_refuel_negative(self):
        """Тест заправки отрицательным количеством."""
        with self.assertRaises(ValueError):
            self.car.refuel_car(-10.0)

    def test_drive_valid(self):
        """Тест корректной поездки."""
        # Сначала заправляем
        self.car.refuel_car(40.0)
        
        # Едем 100 км (потратится 8 литров)
        remaining_fuel = self.car.drive(100.0)
        self.assertAlmostEqual(remaining_fuel, 32.0, places=2)
        
        # Едем ещё 200 км (потратится 16 литров)
        remaining_fuel = self.car.drive(200.0)
        self.assertAlmostEqual(remaining_fuel, 16.0, places=2)

    def test_drive_insufficient_fuel(self):
        """Тест поездки без достаточного количества топлива."""
        self.car.refuel_car(10.0)  # Заправляем только 10 литров
        
        # Пытаемся проехать 200 км (нужно 16 литров)
        with self.assertRaises(ValueError) as context:
            self.car.drive(200.0)
        self.assertIn("Недостаточно топлива", str(context.exception))

    def test_drive_negative_distance(self):
        """Тест поездки на отрицательное расстояние."""
        with self.assertRaises(ValueError):
            self.car.drive(-50.0)

    def test_drive_zero_distance(self):
        """Тест поездки на нулевое расстояние."""
        self.car.refuel_car(20.0)
        remaining_fuel = self.car.drive(0.0)
        self.assertAlmostEqual(remaining_fuel, 20.0, places=2)

    def test_complete_scenario(self):
        """Полный сценарий: заправка -> поездка -> заправка."""
        # Начальное состояние
        self.assertEqual(self.car.get_current_fuel_level(), 0.0)
        
        # Заправка
        self.car.refuel_car(50.0)
        self.assertAlmostEqual(self.car.get_current_fuel_level(), 50.0, places=2)
        
        # Поездка
        remaining = self.car.drive(300.0)  # 300 км * 0.08 = 24 литра
        self.assertAlmostEqual(remaining, 26.0, places=2)  # 50 - 24 = 26
        
        # Ещё одна заправка
        self.car.refuel_car(20.0)
        self.assertAlmostEqual(self.car.get_current_fuel_level(), 46.0, places=2)
        
        # Последняя поездка
        remaining = self.car.drive(500.0)  # 500 км * 0.08 = 40 литров
        self.assertAlmostEqual(remaining, 6.0, places=2)  # 46 - 40 = 6


if __name__ == "__main__":
    unittest.main()
