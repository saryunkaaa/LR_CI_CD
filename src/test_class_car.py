import unittest
from car import Car, TooMuchFuelError, NotEnoughFuelError

class TestCar(unittest.TestCase):
    
    def setUp(self):
        self.car = Car("TestModel", 80)
    
    def test_empty_on_start(self):
        self.assertEqual(self.car.get_current_fuel_level(), 0)
    
    def test_refuel_30(self):
        self.car.refuel_car(30)
        self.assertEqual(self.car.get_current_fuel_level(), 30)
    
    def test_refuel_50(self):
        self.car.refuel_car(50)
        self.assertEqual(self.car.get_current_fuel_level(), 50)
    
    def test_refuel_negative(self):
        with self.assertRaises(ValueError):
            self.car.refuel_car(-10)
    
    def test_refuel_too_much(self):
        with self.assertRaises(TooMuchFuelError):
            self.car.refuel_car(100)
    
    def test_drive_with_enough_fuel(self):
        self.car.refuel_car(40)
        remaining_fuel = self.car.drive(200)
        expected_fuel = 40 - 8 * (200 / 100)
        self.assertEqual(remaining_fuel, expected_fuel)
    
    def test_drive_without_enough_fuel(self):
        self.car.refuel_car(10)
        with self.assertRaises(NotEnoughFuelError):
            self.car.drive(200)
    
    def test_drive_negative_distance(self):
        with self.assertRaises(ValueError):
            self.car.drive(-100)
    
    def test_multiple_refuels(self):
        self.car.refuel_car(30)
        self.car.refuel_car(20)
        self.assertEqual(self.car.get_current_fuel_level(), 50)
    
    def test_drive_and_refuel(self):
        self.car.refuel_car(40)
        self.car.drive(100)
        remaining = self.car.get_current_fuel_level()
        self.car.refuel_car(20)
        self.assertEqual(self.car.get_current_fuel_level(), remaining + 20)
