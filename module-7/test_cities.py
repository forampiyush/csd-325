import unittest
from city_functions import city_country


class CityTestCase(unittest.TestCase):

    def test_city_country(self):
        formatted = city_country("santiago", "chile")
        self.assertEqual(formatted, "Santiago, Chile")


if __name__ == "__main__":
    unittest.main()