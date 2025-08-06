import unittest
from api_gestion_dispositivos import *

class TestAPI(unittest.TestCase):
    def test_listar_dispositivos(self):
        response = listar_dispositivos()
        self.assertEqual(response.status_code, 200)

    def test_agregar_dispositivo(self):
        data = {"name": "Router", "job": "Core"}
        response = agregar_dispositivo(data)
        self.assertEqual(response.status_code, 201)

    def test_actualizar_dispositivo(self):
        data = {"name": "Switch", "job": "Access"}
        response = actualizar_dispositivo(2, data)
        self.assertIn(response.status_code, [200, 201])

    def test_eliminar_dispositivo(self):
        response = eliminar_dispositivo(2)
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
