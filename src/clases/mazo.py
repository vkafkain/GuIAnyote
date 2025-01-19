import random
from carta import Carta
from constants.contants import PALOS, VALORES
from jugador import Jugador

class Mazo:
  def __init__(self):
    self.cartas = [Carta(palo,valor) for palo in self.PALOS for valor in self.VALORES]
  
  def barajar(self):
    random.shuffle(self.cartas)

  
  def repartir(self, numero_jugadores):
    if numero_jugadores <= 0:
      raise ValueError("Debe haber almenos un jugador.")
    
    cartas_por_jugador = 6
    total_cartas_necesarias = numero_jugadores*cartas_por_jugador

    manos = [self.cartas[i * cartas_por_jugador : (i + 1) * cartas_por_jugador] 
             for i in range(numero_jugadores)]

    # Eliminar las cartas repartidas del mazo
    self.cartas = self.cartas[total_cartas_necesarias:]

  # def repartir_cartas_restantes(self, jugadores):
  #   for jugador in jugadores:
  #     while len(jugador)

  def __str__(self):
      return f"Mazo con {len(self.cartas)} cartas"

  