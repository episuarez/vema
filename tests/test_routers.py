import unittest

from vema.src.routers import name_to_def, name_to_uri, generate_routers

class Routers_Tests(unittest.TestCase):
    def test_generate_routers(self):
        generate_routers();

    def test_name_to_uri(self):
        self.assertEqual(name_to_uri("esto es una prueba"), "esto-es-una-prueba");
        self.assertNotEqual(name_to_uri("esto es una prueba"), "esto es una prueba");
        self.assertNotEqual(name_to_uri("esto es una prueba"), "esto%20es%20una%20prueba");

    def test_name_to_def(self):
        self.assertEqual(name_to_def("esto es una prueba"), "esto_es_una_prueba");
        self.assertNotEqual(name_to_def("esto es una prueba"), "esto es una prueba");
        self.assertNotEqual(name_to_def("esto es una prueba"), "esto%20es%20una%20prueba");

if __name__ == "__main__":
    unittest.main();