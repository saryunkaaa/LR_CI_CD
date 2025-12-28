import unittest
from car import Car

class TestCar(unittest.TestCase):
    
    def setUp(self):
        self.car = Car("Toyota", 60.0)
    
    def test_initial_fuel(self):
        self.assertEqual(self.car.current_fuel, 0.0)
    
    def test_refuel_normal(self):
        self.car.refuel(30.0)
        self.assertEqual(self.car.current_fuel, 30.0)
    
    def test_refuel_too_much(self):
        with self.assertRaises(ValueError):
            self.car.refuel(70.0)
    
    def test_refuel_negative(self):
        with self.assertRaises(ValueError):
            self.car.refuel(-10.0)
    
    def test_drive_success(self):
        self.car.refuel(40.0)
        result = self.car.drive(100.0)
        self.assertIn("Проехали 100.0 км", result)
        self.assertAlmostEqual(self.car.current_fuel, 32.0, places=1)
    
    def test_drive_no_fuel(self):
        with self.assertRaises(ValueError):
            self.car.drive(10.0)
    
    def test_get_fuel_info(self):
        self.car.refuel(25.5)
        info = self.car.get_fuel_info()
        self.assertEqual(info, "Toyota: 25.5/60.0 л")
    
    def test_multiple_operations(self):
        self.car.refuel(50.0)
        self.car.drive(200.0)
        self.car.refuel(10.0)
        self.assertAlmostEqual(self.car.current_fuel, 44.0, places=1)

if __name__ == "__main__":
    unittest.main()
