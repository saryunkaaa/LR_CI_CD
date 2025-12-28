import unittest
import sys
import os

# Добавляем путь к текущей директории
sys.path.insert(0, os.path.dirname(__file__))

# Теперь импортируем
from car import hello_world

class TestCar(unittest.TestCase):
    def test_hello(self):
        result = hello_world()
        self.assertEqual(result, "Hello World from Car!")

if __name__ == '__main__':
    unittest.main()
