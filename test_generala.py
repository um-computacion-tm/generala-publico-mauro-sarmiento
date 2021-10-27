import unittest
from generala import Jugadores, Dados, Tabla, Generala


class TestJugadores(unittest.TestCase):     

    def test_agregar_jugadores(self):
        jugadores_e = Jugadores()
        jugadores_e.cantidad = 2
        jugadores_e.jugadores = ['Agustín', 'Mauro']
        self.assertEqual(len(jugadores_e.jugadores), 2)
    
    def test_agregar_jugadores_II(self):
        jugadores_e = Jugadores()
        jugadores_e.cantidad = 3
        jugadores_e.jugadores = ['Agustín', 'Mauro', 'Bruno']
        self.assertEqual(len(jugadores_e.jugadores), 3)

    def test_agregar_jugadores_III(self):
        jugadores_e = Jugadores()
        jugadores_e.cantidad = 4
        jugadores_e.jugadores = ['Agustín', 'Mauro', 'Bruno', 'Nico']
        self.assertEqual(len(jugadores_e.jugadores), 4)

    def test_agregar_jugadores_IV(self):
        jugadores_e = Jugadores()
        jugadores_e.cantidad = 5
        jugadores_e.jugadores = ['Agustín', 'Mauro', 'Bruno', 'Nico', 'Tobi']
        self.assertEqual(len(jugadores_e.jugadores), 5)

class TestDados(unittest.TestCase):         
    
    def test_tirada(self):
        dados_e = Dados()
        dados_e.realizar_tirada()
        self.assertEqual(len(dados_e.dados), 5)
        
    def test_dadinios(self):
        dados_e = Dados()
        dados_e.realizar_tirada()
        dados_e.dados = [2,2,2,4,5]
        self.assertEqual((dados_e.dados), [2,2,2,4,5])
        
    def test_apartar_dados(self):
        dados_e = Dados()
        dados_e.realizar_tirada()
        dados_e.dados = [2,2,2,4,5]
        dados_e.apartar_dados()
        self.assertEqual((dados_e.repetidos), [2,2,2,2,2,2])

    def test_apartar_dados_II(self):
        dados_e = Dados()
        dados_e.realizar_tirada()
        dados_e.dados = [1,2,2,4,5]
        dados_e.apartar_dados()
        self.assertEqual((dados_e.repetidos), [2,2])

    def test_apartar_dados_II(self):
        dados_e = Dados()
        dados_e.realizar_tirada()
        dados_e.dados = [2,2,2,2,1]
        dados_e.apartar_dados()
        self.assertEqual((dados_e.repetidos), [2,2,2,2,2,2,2,2,2,2,2,2])

    def test_apartar_dados_III(self):
        dados_e = Dados()
        dados_e.realizar_tirada()
        dados_e.dados = [1,2,3,4,5]
        dados_e.apartar_dados()
        self.assertEqual((dados_e.repetidos), [])

    def test_ordenar_repetidos(self):
        dados_e = Dados()
        dados_e.realizar_tirada()
        dados_e.dados = [2,2,2,4,5]
        dados_e.apartar_dados()
        dados_e.ordenar_repetidos()
        self.assertEqual((dados_e.repetidos), [2,2,2])

    def test_ordenar_repetidos_I(self):
        dados_e = Dados()
        dados_e.realizar_tirada()
        dados_e.dados = [1,2,3,4,5]
        dados_e.apartar_dados()
        dados_e.ordenar_repetidos()
        self.assertEqual((dados_e.repetidos), [])

    def test_ordenar_repetidos_len_I(self):
        dados_e = Dados()
        dados_e.realizar_tirada()
        dados_e.dados = [2,2,2,4,5]
        dados_e.apartar_dados()
        dados_e.ordenar_repetidos()
        self.assertEqual(len(dados_e.repetidos), 3)
        
    def test_ordenar_repetidos_len_II(self):
        dados_e = Dados()
        dados_e.realizar_tirada()
        dados_e.dados = [2,2,4,4,5]
        dados_e.apartar_dados()
        dados_e.ordenar_repetidos()
        self.assertEqual(len(dados_e.repetidos), 4)

    def test_ordenar_repetidos_len_III(self):
        dados_e = Dados()
        dados_e.realizar_tirada()
        dados_e.dados = [1,3,3,4,5]
        dados_e.apartar_dados()
        dados_e.ordenar_repetidos()
        self.assertEqual(len(dados_e.repetidos), 2)

    def test_sumar_dados(self):
        dados_e = Dados()
        dados_e.realizar_tirada()
        dados_e.dados = [2,2,2,4,6]
        dados_e.apartar_dados()
        dados_e.ordenar_repetidos()
        dados_e.sumar_dados()
        self.assertEqual((dados_e.puntaje_c), 16)

    def test_sumar_dados_II(self):
        dados_e = Dados()
        dados_e.realizar_tirada()
        dados_e.dados = [6,6,6,6,6]
        dados_e.apartar_dados()
        dados_e.ordenar_repetidos()
        dados_e.sumar_dados()
        self.assertEqual((dados_e.puntaje_c), 30)

    def test_determinar_categoria_sin_categoria(self):
        dados_e = Dados()
        dados_e.realizar_tirada()
        dados_e.dados = [1,2,2,4,5]
        dados_e.apartar_dados()
        dados_e.ordenar_repetidos()
        dados_e.determinar_categoria()
        self.assertEqual((dados_e.cat), 'Sin categoria')

    def test_determinar_categoria_poker(self):
        dados_e = Dados()
        dados_e.realizar_tirada()
        dados_e.dados = [1,1,1,1,2]
        dados_e.apartar_dados()
        dados_e.ordenar_repetidos()
        dados_e.determinar_categoria()
        self.assertEqual((dados_e.cat), 'Poker')

    def test_determinar_categoria_full(self):
        dados_e = Dados()
        dados_e.realizar_tirada()
        dados_e.dados = [2,2,2,4,4]
        dados_e.apartar_dados()
        dados_e.ordenar_repetidos()
        dados_e.determinar_categoria()
        self.assertEqual((dados_e.cat), 'Full')

    def test_determinar_categoria_generala(self):
        dados_e = Dados()
        dados_e.realizar_tirada()
        dados_e.dados = [3,3,3,3,3]
        dados_e.apartar_dados()
        dados_e.ordenar_repetidos()
        dados_e.determinar_categoria()
        self.assertEqual((dados_e.cat), 'Generala')

    def test_determinar_categoria_escalera(self):
        dados_e = Dados()
        dados_e.realizar_tirada()
        dados_e.dados = [1,2,3,4,5]
        dados_e.apartar_dados()
        dados_e.ordenar_repetidos()
        dados_e.determinar_categoria()
        self.assertEqual((dados_e.cat), 'Escalera')

class TestTabla(unittest.TestCase):         

    def test_generar_tabla(self):
        tabla_u = Tabla()
        jugadores = Jugadores()
        jugadores.cantidad = 2
        jugadores.jugadores = ['Agustin','Mauro']
        tabla_u.generar_tabla()
        self.assertEqual(len(tabla_u.tabla), 2)    #! Error: No suma elementos a las listas

    def test_tabla_final(self):
        tabla = Tabla()
        jugadores = Jugadores()
        jugadores.cantidad = 2
        jugadores.jugadores = ['Agustin','Mauro']
        tabla.generar_tabla()
        tabla.iniciar_juego()
        tabla.tabla_final()
        self.assertEqual(len(tabla.tabla), 2)

class TestGenerala(unittest.TestCase):   

    def test_iniciar_juego(self):
        generala_e = Generala()
        tabla_e = Tabla()
        jugadores_n = Jugadores()
        generala_e.iniciar_juego()
        jugadores_n.cantidad = 2
        jugadores_n.jugadores = ['Agustin','Mauro']
        self.asserEqual(len(tabla_e.orden_final), 2)

    def test_iniciar_juego_II(self):
        tabla_e = Tabla()
        jugadores_n = Jugadores()
        generala_e = Generala()
        generala_e.iniciar_juego()
        jugadores_n.cantidad = 3
        jugadores_n.jugadores = ['Agustin','Mauro','Bruno']
        self.asserEqual(len(tabla_e.orden_final), 3)

    def test_iniciar_juego_III(self):
        tabla_e = Tabla()
        jugadores_n = Jugadores()
        generala_e = Generala()
        generala_e.iniciar_juego()
        jugadores_n.cantidad = 4
        jugadores_n.jugadores = ['Agustin','Mauro','Bruno','Nico']
        self.asserEqual(len(tabla_e.orden_final), 4)

    def test_iniciar_juego_IV(self):
        tabla = Tabla()
        jugadores = Jugadores()
        generala_e = Generala()
        jugadores.cantidad = 5
        jugadores.jugadores = ['Agustin','Mauro','Bruno','Nico','Tobias']
        generala_e.iniciar_juego()
        self.asserEqual(len(tabla.orden_final), 5)

    def test_victoria(self):
        dados_u = Dados()
        tabla_n = Tabla()
        jugadores_r = Jugadores()
        generala_z = Generala ()
        jugadores_r.cantidad = 3
        jugadores_r.jugadores = ['Agustin','Mauro','Bruno']
        generala_z.bienvenida()
        dados_u.dados = [5,5,5,5,5]
        generala_z.turnos()
        generala_z.victoria()
        self.assertEqual()
        
        
if __name__ == '__main__':
    unittest.main()