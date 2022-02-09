import random

class Carta(object):
    """ En el fondo, una carta es sólo un pedazo de cartón """
    def __init__(self):
        pass
    def __str__(self):
        return "Esta carta está en blanco"

class Comodin(Carta):
    def __str__(self):
        return "Comodín"

class Naipe(Carta):
    """
    Lo que diferencia a un naipe de otras cartas es poseer un palo
    y un rango
    """
    def __init__(self, palo, rango):
        """
        palo : str, el nombre del palo
        rango : int (usualmente), el número sobre la carta
        tanto palo, como rango deben tener un método __str__,
        en la versión analógica estos datos están impresos sobre la carta...
        """
        self.palo = palo
        self.rango = rango
    def getPalo(self):
        return self.palo
    def getRango(self):
        return self.rango
    def __str__(self):
        return (str(self.palo) + " " + str(self.rango))

class ColeccionDeCartas(object):
    def __init__(self, cartas = []):
        """
        cartas es una lista de cartas; arma la colección con la lista
        dada
        """
        self.cartas = cartas
        # self.mezclado = False
    def armarColeccion(self, cartas):
        self.cartas = cartas
        # self.mezclado = False
    def getCartas(self):
        return self.cartas[:]
    def agregarCarta(self, carta):
        self.cartas.append(carta)
    def contarCartas(self):
        return len(self.cartas)
    def darUnaCarta(self):
        """
        representa la acción de dar vuelta la primera carta arriba del
        pilón, es decir, la última carta de la lista
        """
        if ( self.contarCartas() > 0 ):
            return self.cartas.pop()
    def darCarta(self, k):
        """
        devuelve la carta en la posición k y la descarta de la
        colección
        """
        try:
            return self.cartas.pop(k)
        except IndexError:
            print("No hay carta en la posición " + str(k), end = '\n')
    def __str__(self):
        s = ''
        for c in self.cartas:
            s += str(c)
            s += ', '
        return s[:-2]

class Mazo(ColeccionDeCartas):
    def __init__(self, cartas = []):
        ColeccionDeCartas.__init__(self, cartas)
        self.mezclado = False
    def estaMezclado(self):
        return self.mezclado
    def armarColeccion(self, cartas):
        ColeccionDeCartas.armarColeccion(self, cartas)
        self.mezclado = False
    def agregarComodines(self, cantidad):
        """ agrega cantidad de comodines al mazo """
        while ( cantidad > 0 ):
            self.agregarCarta(Comodin())
            cantidad -= 1
        self.mezclado = False
    def mezclarMazo(self):
        """ modifica la lista self.cartas """
        if ( not (self.mezclado) ):
            l = self.contarCartas()
            while ( l > 0 ):
                c = self.darCarta(random.choice(range(l)))
                self.agregarCarta(c)
                l -= 1
        self.mezclado = True

def crearNaipes(palos, rangos):
    """
    devuelve una lista de naipes cuyos palos y rangos están en la lista palos
    y dentro del rango rangos
    """
    naipes = []
    for palo in palos:
            for rango in rangos:
                naipes.append(Naipe(palo, rango))
    return naipes

def crearPalo(palo, rangos):
    """
    palo : str, el nombre del palo
    rangos : una lista u objeto sobre el cual iterar, que contiene los
    rangos dentro del palo
    """
    return crearNaipes([palo], rangos)


class MazoDeNaipes(Mazo):
    def __init__(self, palos, naipes):
        """ asume que naipes es una lista de naipes """
        Mazo.__init__(self, naipes)
        # for c in naipes:
            # if ( not (c.palo in palos) ):
                #palos.append(palo)
        self.palos = palos
    def getPalos(self):
        return self.palos

class MazoEspagnol(MazoDeNaipes):
    def __init__(self):
        palos = ["copas", "espadas", "oros", "bastos"]
        self.rangos = range(1,13) # números del 1 al 12
        naipes = crearNaipes(palos, self.rangos)
        MazoDeNaipes.__init__(self, palos, naipes)

class MazoEspagnolCorto(MazoEspagnol):
    def __init__(self):
        MazoEspagnol.__init__(self)
        # sacar ochos y nueves
        k = self.contarCartas() - 1
        while ( l >= 0 ):
            if ( self.cartas[k].rango == 8 or self.cartas[k].rango == 9 ):
                self.darCarta(k)
            k -= 1

class MazoFrances(MazoDeNaipes):
    def __init__(self):
        palos = ["corazones", "picas", "diamantes", "tréboles"]
        self.rangos = range(1,14)
        naipes = crearNaipes(palos, self.rangos)
        MazoDeNaipes.__init__(self, palos, naipes)
