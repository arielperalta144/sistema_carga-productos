import sqlite3


class conexionDB:
    def __init__(self):
        self.base_datos = 'database/articulos.db'
        self.conexion = None
        self.cursor = None
        self.conectar()

    def conectar(self):
        try:
            self.conexion = sqlite3.connect(self.base_datos)
            self.cursor = self.conexion.cursor()
        except sqlite3.Error as e:
            print(f"Error al conectar a la base de datos: {e}")

    def cerrar(self):
        if self.conexion:
            try:
                self.conexion.commit()
                self.conexion.close()
            except sqlite3.Error as e:
                print(f"Error al cerrar la conexión: {e}")

    def __enter__(self):
        self.conectar()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cerrar()
