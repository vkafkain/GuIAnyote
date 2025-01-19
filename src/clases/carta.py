
class Carta:
  def __init__(self, palo, valor):
      
        self.palo = palo
        self.valor = valor

  def __str__(self):
        return f"{self.valor} de {self.palo}"

  def __repr__(self):
        return f"Carta(palo='{self.palo}', valor='{self.valor}')"
