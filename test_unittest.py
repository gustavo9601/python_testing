import unittest

from shopping_cart import Item, ShoppingCart, NotExistItemErrorExeception


class TestShoppingCart(unittest.TestCase):

    # Metodo que se ejecutara antes de cada una de las pruebas
    def setUp(self):
        # print("Setup Antes de la prueba")
        self.pan = Item('Pan', 500)
        self.jugo = Item('Jugo', 1000)
        self.shopping_cart = ShoppingCart()
        # adding an item to the cart
        self.shopping_cart.add_item(self.pan)

    # Meotodo que se ejecutara despues de cada una de las pruebas
    def tearDown(self):
        # print("tearDown Despues de la prueba")
        pass

    def test_cinco_mas_cinco_igual_diez(self):
        self.assertEqual(5 + 5, 10)

    def test_nombre_producto_igual_pan(self):
        self.assertEqual(self.pan.name, 'Pan')

    def test_nombre_producto_diferente_pan(self):
        self.assertNotEqual(self.pan.name, 'manzana')

    def test_el_carrito_tiene_productos(self):
        # Verifica que sea verdadero
        self.assertTrue(self.shopping_cart.contains_items())

    def test_no_contiene_productos_el_carrito(self):
        self.shopping_cart.remove_item(self.pan)
        self.assertFalse(self.shopping_cart.contains_items())

    def test_obtener_producto_pan(self):
        item = self.shopping_cart.get_item(self.pan)
        # Valida que el tipo de objeto sea el mismo
        self.assertIs(item, self.pan)
        self.assertIsNot(item, self.jugo)

    def test_obtener_execpcion_al_obtener_jugo(self):
        # Forzando una exepcion, y validar que si sea levanta una exepcion
        with self.assertRaises(NotExistItemErrorExeception):
            self.shopping_cart.get_item(self.jugo)

    def test_total_con_un_producto_en_el_carrito(self):
        total = self.shopping_cart.total()
        # verifica que sea mayor el parametro de la izquierda al de la derecha
        self.assertGreater(total, 0)
        # menor a
        self.assertLess(total, 1000)

        self.assertEqual(total, self.pan.price)

        # Permite crear asserciones personalizadas
        if total == 0:
            self.fail('El total dio 0 =(')

    def test_codigo_pan(self):
        # Permite verificar que el parametro derecho si este contenido en el izquierdo
        self.assertRegex(self.pan.code(), self.pan.name)

    # Prueba que sera skip, y como parametro se enviara la razon del skip
    @unittest.skip('Es una prubea, y por eso se salta')
    def test_prueba_skip(self):
        pass

    # Prueba que sera skip, y como parametro se enviara la condicion a dejecucion y el motivo de skip
    # @unittest.skipIf(<<Condicion>>, <<Razon>>)
    @unittest.skipIf(True, 'Es una prubea, y por eso se salta')
    def test_prueba_skip_condicional(self):
        pass



if __name__ == '__main__':
    # Se ejecutaran todas las pruebas unitarias
    # por consola para mas detalle
    # py test_unittest.py -v

    # Para covertura
    # coverage run <<file_name_tests>>.py

    # ver el reporte de convertura
    # coverage report <<file_name>>.py

    # Ver el reporte de convertura, mostrando las lineas sin covertura
    # coverage report -m <<file_name>>.py

    # Exportando el coverage a html
    # coverage html <<file_name>>.py

    # Levantando un servidor lite en PY para ver el reporte
    # py -m http.server

    unittest.main()
