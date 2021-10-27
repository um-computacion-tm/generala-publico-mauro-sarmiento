import random
import operator

class Jugadores:
    
    def __init__(self):
        self.jugadores = []
        self.cantidad = 0        
        self.jugador = ''

    def agregar_jugadores(self):                                                      #* Se ingresan entre 2 y 5 jugadores
        while not (2 <= self.cantidad <= 5):
            self.cantidad = int(input('¿Cuantos jugadores hay? (2-5): '))
            print('-'*33)
        for l in range(self.cantidad):
            self.jugador = str(input('Ingrese nombre del Jugador: '))
            self.jugadores.append(self.jugador)
        print('-' *33)
        return self.jugadores

class Dados:
    
    def __init__(self):
        self.dados = []
        self.dado = 0
        self.numero = 5
        self.repetidos = []
        self.puntaje_c = 0
        self.cat = ''

    def realizar_tirada(self):                                                       #* Devuelve una lista con 5 numeros al azar comprendidos entre 1 y 6
        for i in range(self.numero):
            self.dado = random.randint(1,6)
            self.dados.append(self.dado)
            self.dados.sort()
        return self.dados
    
    def apartar_dados(self):                                                         #* Verifica los repetidos y los aparta para el usuario                        
        for q in range(len(self.dados)):
            value = self.dados[q]
            for t in range(len(self.dados)):
                value_2 = self.dados[t]
                if q == t:
                    continue
                elif value == value_2:
                    self.repetidos.append(value_2)
    
    def ordenar_repetidos(self):                                                     #* Solución a un bug, en el que las listas con 3 o mas valores repetidos
        if len(self.repetidos) == 16:                                                #* duplicaban su longitud
            for pos in range(8):
                self.repetidos.pop(pos)
            for pos in range(len(self.repetidos)-4):
                self.repetidos.pop(pos)
            self.repetidos.append(self.dados[0])
            self.repetidos.sort()
        if len(self.repetidos) == 12:
            for pos in range(5):
                self.repetidos.pop(pos)
            for pos in range(len(self.repetidos)-4):
                self.repetidos.pop(pos)
        if len(self.repetidos) > 4 and len(self.repetidos) < 7 and len(self.repetidos) != 5:
            for pos in range(len(self.repetidos)-3):
                self.repetidos.pop(pos)

    def sumar_dados(self):                                                           #* Suma el puntaje total de la jugada
        self.puntaje_c = sum(self.dados) - sum(self.repetidos)

    def determinar_categoria(self):  
                                                        #* Determina la categoria de la tirada final en base al numero repetido de dados
        self.contador_1 = 1
        self.contador_2 = 0
        for h in range(4):
            if self.dados[h] == self.dados[h-1]:
                self.contador_1 += 1
            else:
                self.contador_2 += 1
        if self.contador_1 == 4 and self.contador_2 == 1:
            self.cat = 'Poker'
            self.puntaje_c += 40
        elif self.contador_1 == 3 and self.contador_2 == 2 and len(self.repetidos) >= 4 or self.contador_1 == 2 and self.contador_2 == 3 and len(self.repetidos) >= 4:
            self.dados_r = self.repetidos
            self.apartar_dados()
            self.ordenar_repetidos()
            if len(self.repetidos) == 5:
                self.cat = 'Full'
                self.puntaje_c += 30
            self.repetidos = self.dados_r       
        elif self.contador_1 == 5:
            self.cat = 'Generala'
            self.puntaje_c += 50
        elif self.dados == [1,2,3,4,5] or self.dados == [2,3,4,5,6] or self.dados == [1,3,4,5,6]:
            self.cat = 'Escalera'
            self.puntaje_c += 20
        else:
            self.cat = 'Sin categoria'

class Tabla:

    def __init__(self):
        self.tabla = []
        self.puntaje_a = []
        self.puntaje_b = []
        self.puntaje_c = []
        self.puntaje_d = []
        self.puntaje_e = []
        self.orden = []
        self.orden_final = {}
        jugadores = Jugadores()
        dados = Dados()
    
    def generar_tabla(self):
        print('--- [Jugador, Puntaje (1)(2)(3)] ---')
        if len(jugadores.jugadores) == 2:
            self.tabla.append(jugadores.jugadores[0])
            self.tabla.append(self.puntaje_a)
            self.tabla.append(jugadores.jugadores[1])
            self.tabla.append(self.puntaje_b)
        if len(jugadores.jugadores) == 3:
            self.tabla.append(jugadores.jugadores[0])
            self.tabla.append(self.puntaje_a)
            self.tabla.append(jugadores.jugadores[1])
            self.tabla.append(self.puntaje_b)
            self.tabla.append(jugadores.jugadores[2])
            self.tabla.append(self.puntaje_c)
        if len(jugadores.jugadores) == 4:
            self.tabla.append(jugadores.jugadores[0])
            self.tabla.append(self.puntaje_a)
            self.tabla.append(jugadores.jugadores[1])
            self.tabla.append(self.puntaje_b)
            self.tabla.append(jugadores.jugadores[2])
            self.tabla.append(self.puntaje_c)
            self.tabla.append(jugadores.jugadores[3])
            self.tabla.append(self.puntaje_d)
        if len(jugadores.jugadores) == 5:
            self.tabla.append(jugadores.jugadores[0])
            self.tabla.append(self.puntaje_a)
            self.tabla.append(jugadores.jugadores[1])
            self.tabla.append(self.puntaje_b)
            self.tabla.append(jugadores.jugadores[2])
            self.tabla.append(self.puntaje_c)
            self.tabla.append(jugadores.jugadores[3])
            self.tabla.append(self.puntaje_d)
            self.tabla.append(jugadores.jugadores[4])
            self.tabla.append(self.puntaje_e)
        print('-'*36)
        return self.tabla

    def iniciar_juego(self):                                                               #* Realiza una tirada y ordena a los jugadores en orden decreciente de puntaje, para determinar el orden de los turnos
        jugadores.agregar_jugadores()
        for n in range (len(jugadores.jugadores)):
            self.puntaje_i = sum(dados.realizar_tirada())
            self.orden.append(self.puntaje_i)
            self.orden_final[jugadores.jugadores[n]] = self.orden[n]
            dados.dados = []
        self.orden_final = sorted(self.orden_final.items(), key=operator.itemgetter(1), reverse = True)   #* Con operator, transforma el diccionario en lista, los ordena mediante el puntaje, y vuelve a convertirlos en diccionario
        print('\n','- El orden de juego respecto a los dados lanzados es',self.orden_final,'-\n')
        print('-'*36)
        input('...(Enter para continuar)...')

    def tabla_final(self):                                                                                #* Asigna las posiciones finales y genera la tabla final
        if len(jugadores.jugadores) == 2:    
            self.jugador_1 = list(self.orden_final[0])[0]
            self.jugador_2 = list(self.orden_final[1])[0]
            jugadores.jugadores[0] = self.jugador_1
            jugadores.jugadores[1] = self.jugador_2
        if len(jugadores.jugadores) == 3:    
            self.jugador_1 = list(self.orden_final[0])[0]
            self.jugador_2 = list(self.orden_final[1])[0]
            self.jugador_3 = list(self.orden_final[2])[0]
            jugadores.jugadores[0] = self.jugador_1
            jugadores.jugadores[1] = self.jugador_2
            jugadores.jugadores[2] = self.jugador_3
        if len(jugadores.jugadores) == 4:    
            self.jugador_1 = list(self.orden_final[0])[0]
            self.jugador_2 = list(self.orden_final[1])[0]
            self.jugador_3 = list(self.orden_final[2])[0]
            self.jugador_4 = list(self.orden_final[3])[0]
            jugadores.jugadores[0] = self.jugador_1
            jugadores.jugadores[1] = self.jugador_2
            jugadores.jugadores[2] = self.jugador_3
            jugadores.jugadores[3] = self.jugador_4
        if len(jugadores.jugadores) == 5:    
            self.jugador_1 = list(self.orden_final[0])[0]
            self.jugador_2 = list(self.orden_final[1])[0]
            self.jugador_3 = list(self.orden_final[2])[0]
            self.jugador_4 = list(self.orden_final[3])[0]
            self.jugador_5 = list(self.orden_final[4])[0]
            jugadores.jugadores[0] = self.jugador_1
            jugadores.jugadores[1] = self.jugador_2
            jugadores.jugadores[2] = self.jugador_3
            jugadores.jugadores[3] = self.jugador_4
            jugadores.jugadores[4] = self.jugador_5


class Turnos:

    def __init__(self):
        self.repetidos = []
        self.dados_final = []
        self.control = 1
        self.sc = 0
        self.pok = 0
        self.full = 0
        self.gen = 0
        self.esc = 0
        self.total_a = 0
        self.total_b = 0
        self.total_c = 0
        self.total_d = 0
        self.total_e = 0
        jugadores = Jugadores()
        dados = Dados()
        tabla = Tabla()

    def turnos(self):                                                                                #* Inicia los turnos
        tabla.iniciar_juego()
        tabla.tabla_final()
        tabla.generar_tabla()
        print(tabla.tabla)
        for turn in range(3):                                                                        #* Hay un total de 3 turnos
            print('\n')
            print('='*22)
            print('| INICIO DEL TURNO',turn+1,'|')
            print('='*22)
            self.control = 0                                                                         #* 'control' ayuda a determinar que usuario esta jugando
            self.puntaje = tabla.puntaje_a
            for jug in range(len(jugadores.jugadores)):                                              #* El turno se repite para la cantidad de jugadores
                if self.control == 1:
                    self.puntaje = tabla.puntaje_b
                if self.control == 2:
                    self.puntaje = tabla.puntaje_c
                if self.control == 3:
                    self.puntaje = tabla.puntaje_d
                if self.control == 4:
                    self.puntaje = tabla.puntaje_e
                dados.dados = []
                dados.repetidos = []
                self.dados_final = []
                dados.numero = 5                                                                      #* Determina el numero inicial de dados, el valor cambia si se conservan dados
                print('\n','-'*42)
                print(' - El jugador que lanza los dados es', list(tabla.orden_final[jug])[0], '-')
                print('','-'*42)
                input('...(Enter para continuar)...')
                dados.realizar_tirada()
                print('\n',' - Dados en primer lanzamiento:',dados.dados)
                dados.apartar_dados()
                dados.ordenar_repetidos()
                if len(dados.repetidos) != 0 and len(dados.repetidos) < 5:                            #* En el caso de haber conservado dados, vuelve a lanzar hasta un maximo de 3 veces con los dados sobrantes
                    print('\n',' -- Los dados', dados.repetidos, 'se encuentran repetidos, ¿desea conservarlos y volver a tirar? --')
                    self.choice = input(str('     (Si / No) ... '))
                    self.choice = self.choice.lower()
                    if self.choice == 'si':
                        self.dados_final.append(dados.repetidos)
                        if len(dados.repetidos) == 4:
                            num2 = dados.repetidos[3]
                            dados.dados = list(filter((num2).__ne__,dados.dados))
                        num = dados.repetidos[0]
                        dados.dados = list(filter((num).__ne__,dados.dados))
                        dados.numero = len(dados.dados)
                        dados.dados = []
                        dados.repetidos = []
                        dados.realizar_tirada()
                        print('\n',' - Dados en segundo lanzamiento:',dados.dados)
                        dados.apartar_dados()
                        dados.ordenar_repetidos()
                        if len(dados.repetidos) != 0:
                            print('\n',' -- Los dados', dados.repetidos, 'se encuentran repetidos, ¿desea conservarlos y volver a tirar? --')
                            self.choice = input(str('     (Si / No) ... '))
                            self.choice = self.choice.lower()
                            if self.choice == 'si':
                                self.dados_final.append(dados.repetidos)
                                if len(dados.repetidos) == 4:
                                    num2 = dados.repetidos[3]
                                    dados.dados = list(filter((num2).__ne__,dados.dados))
                                num = dados.repetidos[0]
                                dados.dados = list(filter((num).__ne__,dados.dados))
                                dados.numero = len(dados.dados)
                                dados.dados = []
                                dados.repetidos = []
                                dados.realizar_tirada()
                                print('\n',' - Dado en tercer lanzamiento:',dados.dados)
                                dados.apartar_dados()
                                dados.ordenar_repetidos()
                        self.dados_final.append(dados.dados)
                        self.dados_final = [item for l in self.dados_final for item in l]
                        self.dados_final.sort()
                        dados.dados = self.dados_final                           #* Se obtiene la lista final de dados
                dados.dados.sort()
                dados.sumar_dados()
                dados.determinar_categoria()
                print('-'*36)
                print('\n','Tirada final:', dados.dados, dados.cat,'\n')
                print('-'*36)
                if dados.cat == 'Sin categoria':                                 #* Se suman los puntajes individuales en base a la categoria, si es generala, el turno se termina
                    self.sc += dados.puntaje_c
                    self.scd = {'Sin categoria',self.sc}
                    if self.scd not in self.puntaje:
                        self.puntaje.append(self.scd)
                    else:
                        self.scd.update({'Sin categoria',self.sc})
                if dados.cat == 'Full':
                    self.full += dados.puntaje_c
                    self.fulld = {'Full',self.full}
                    if self.fulld not in self.puntaje:
                        self.puntaje.append(self.fulld)
                    else:
                        self.fulld.update({'Full',self.full})
                if dados.cat == 'Poker':
                    self.pok += dados.puntaje_c
                    self.pokd = {'Poker',self.pok}
                    if self.pokd not in self.puntaje:
                        self.puntaje.append(self.pokd)
                    else:
                        self.pokd.update({'Full',self.full})
                if dados.cat == 'Escalera':
                    self.esc += dados.puntaje_c
                    self.escd = {'Escalera',self.esc}
                    if self.escd not in self.puntaje:
                        self.puntaje.append(self.escd)
                    else:
                        self.escd.update({'Escalera',self.esc})
                if dados.cat == 'Generala':
                    self.gen += dados.puntaje_c
                    self.gend = {'Generala',self.gen}
                    if self.gend not in self.puntaje:
                        self.puntaje.append(self.gend)
                    else:
                        self.gend.update({'Generala',self.gen})
                    break
                print('\n',' -- El turno de', list(tabla.orden_final[jug])[0], 'ha terminado --')
                if self.control == 0:                                                              #* Lleva la contabilidad de los puntos totales por turno
                    self.total_a += (self.sc+self.full+self.pok+self.gen+self.esc)
                if self.control == 1:
                    self.total_b += (self.sc+self.full+self.pok+self.gen+self.esc)
                if self.control == 2:
                    self.total_c += (self.sc+self.full+self.pok+self.gen+self.esc)
                if self.control == 3:
                    self.total_d += (self.sc+self.full+self.pok+self.gen+self.esc)
                if self.control == 4:
                    self.total_e += (self.sc+self.full+self.pok+self.gen+self.esc)
                self.control += 1
                dados.puntaje_c = 0
                self.sc = 0
                self.full = 0
                self.pok = 0
                self.gen = 0
                self.esc = 0
            print('\n','-'*33)
            print('--- [Jugador, Puntaje (1)(2)(3)] ---')
            print(tabla.tabla)
            print('-'*33)
            input('...(Enter para continuar)...')

class Generala(Turnos):
    
    def bienvenida(self):
        print('='*20)
        print('|     Generala     |')
        print('='*20)

    def victoria(self):                                                                     #* Condiciones de victoria, generala o mayor cantidad de puntos
        print('\n','='*36)
        if dados.cat == 'Generala':
            if self.control == 0:
                print(' | El ganador es',jugadores.jugadores[0],'con Generala |')
            if self.control == 1:
                print(' | El ganador es',jugadores.jugadores[1],'con Generala |')
            if self.control == 2:
                print(' | El ganador es',jugadores.jugadores[2],'con Generala |')
            if self.control == 3:
                print(' | El ganador es',jugadores.jugadores[3],'con Generala |')
            if self.control == 4:
                print(' | El ganador es',jugadores.jugadores[4],'con Generala |')
        else:
            if self.total_a > self.total_b and self.total_a > self.total_c and self.total_a > self.total_d and self.total_a > self.total_e:
                print(' | El ganador es',jugadores.jugadores[0],'con',self.total_a,'puntos |')
            if self.total_b > self.total_a and self.total_b > self.total_c and self.total_b > self.total_d and self.total_b > self.total_e:
                print(' | El ganador es',jugadores.jugadores[1],'con',self.total_b,'puntos |')
            if self.total_c > self.total_b and self.total_c > self.total_a and self.total_c > self.total_d and self.total_c > self.total_e:
                print(' | El ganador es',jugadores.jugadores[2],'con',self.total_c,'puntos |')
            if self.total_d > self.total_b and self.total_d > self.total_c and self.total_d > self.total_a and self.total_d > self.total_e:
                print(' | El ganador es',jugadores.jugadores[3],'con',self.total_d,'puntos |')
            if self.total_e > self.total_b and self.total_e > self.total_c and self.total_e > self.total_d and self.total_e > self.total_a:
                print(' | El ganador es',jugadores.jugadores[4],'con',self.total_e,'puntos |')
        print('','='*36)
            
if __name__ == '__main__':
    dados = Dados()
    jugadores = Jugadores()
    tabla = Tabla()
    turnos = Turnos()
    juego = Generala()
    juego.bienvenida()
    turnos.turnos()
    juego.victoria()
    input('...(Enter para finalizar)...')