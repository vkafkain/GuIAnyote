from db.ddbb_manager import crear_base_datos, insertar_cartas, cargar_mazo_de_db
from constants.contants import MAZO

crear_base_datos()

insertar_cartas(MAZO)

mazo_desde_db = cargar_mazo_de_db()

print("Mazo cargado desde la base de datos:")
for carta in mazo_desde_db:
    print(carta)

