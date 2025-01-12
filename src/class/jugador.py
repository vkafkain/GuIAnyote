
class Jugador:
    def __init__(self, nombre, es_ia=False):
        
        self.nombre = nombre
        self.es_ia = es_ia
        self.mano = []
        self.puntos = 0
        self.bazas_ganadas = []
      #  self.equipo = None #para próximas versiones

    def jugar_carta(self):
        
        if self.mano:
            return self.mano.pop(0)
        