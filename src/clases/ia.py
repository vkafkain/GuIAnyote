from clases.jugador import Jugador 

class IA(Jugador):
   def __init__(self, nombre):
        super().__init__(nombre, es_ia=True)

   def jugar_carta(self):
        
        # Lógica de IA para seleccionar la mejor carta

        # Por ahora, selecciona la primera carta como ejemplo
        if self.cartas_en_mano:
            return self.cartas_en_mano.pop(0)
        return None
