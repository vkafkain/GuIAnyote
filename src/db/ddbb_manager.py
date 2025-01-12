import sqlite3

DB_FILE = "guinyote.db"

def crear_base_datos():
  conn = sqlite3.connect(DB_FILE)
  c = conn.cursor()
  # Crear tabla de cartas del guiñote si no existe
  c.execute('''CREATE TABLE IF NOT EXISTS cartas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            palo TEXT NOT NULL,
            valor TEXT NOT NULL,
            UNIQUE(palo, valor)              
        )
    '''
            )
    # Crear tabla de partidas
  c.execute('''CREATE TABLE IF NOT EXISTS partidas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha_inicio DATETIME NOT NULL,
            fecha_fin DATETIME,
            resultado TEXT,
            equipo1_puntos INTEGER,
            equipo2_puntos INTEGER
        )''')
    # Crear tabla de jugadores
  c.execute('''CREATE TABLE IF NOT EXISTS jugadores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            es_ia BOOLEAN NOT NULL DEFAULT 0,
            partidas_jugadas INTEGER DEFAULT 0,
            partidas_ganadas INTEGER DEFAULT 0,
            puntos_acumulados INTEGER DEFAULT 0
        )''')
    # Crear tabla de movimientos
  c.execute('''CREATE TABLE IF NOT EXISTS movimientos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            partida_id INTEGER NOT NULL,
            jugador_id INTEGER NOT NULL,
            carta_jugada TEXT NOT NULL,
            orden INTEGER NOT NULL,
            FOREIGN KEY (partida_id) REFERENCES partidas(id),
            FOREIGN KEY (jugador_id) REFERENCES jugadores(id)
        )''')
    # Crear tabla de bazas
  c.execute('''CREATE TABLE IF NOT EXISTS bazas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            partida_id INTEGER NOT NULL,
            equipo_ganador TEXT NOT NULL,
            cartas TEXT NOT NULL,
            FOREIGN KEY (partida_id) REFERENCES partidas(id)
        )''')  
  conn.commit()
  conn.close()
  print("Base de datos y tablas creadas correctamente.")

def insertar_cartas(mazo):
    """Inserta todas las cartas en la base de datos."""
    conexion = sqlite3.connect("guinyote.db")
    cursor = conexion.cursor()

    for palo, valor in mazo:
      cursor.execute("INSERT INTO cartas (palo, valor) VALUES (?, ?)", (palo, valor))

    conexion.commit()
    conexion.close()


def cargar_mazo_de_db():
    conexion = sqlite3.connect("guinyote.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT palo, valor FROM cartas")
    mazo = cursor.fetchall()
    conexion.close()
    return mazo

# añadir funciones adicionales para las tablas como registrar_partida, agregar_jugador etc..
