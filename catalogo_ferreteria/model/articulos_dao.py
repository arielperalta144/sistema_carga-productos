from .conexion_db import conexionDB
from tkinter import messagebox


def crear_tabla():
    sql = '''
        CREATE TABLE IF NOT EXISTS articulos (
            id_articulos INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(100) NOT NULL,
            proveedor TEXT,
            categoria VARCHAR(50),
            precio DECIMAL(10, 2),
            stock INTEGER
        );
    '''
    try:
        with conexionDB() as cursor:
            cursor.execute(sql)
    except Exception as e:
        titulo = 'Crear Registro'
        mensaje = f'Error al crear la tabla: {e}'
        messagebox.showerror(titulo, mensaje)


def borrar_tabla():
    sql = 'DROP TABLE IF EXISTS articulos'
    try:
        with conexionDB() as cursor:
            cursor.execute(sql)
        titulo = 'Borrar Registro'
        mensaje = 'Se borró la tabla con éxito'
        messagebox.showinfo(titulo, mensaje)
    except Exception as e:
        titulo = 'Borrar Registro'
        mensaje = f'Error al borrar la tabla: {e}'
        messagebox.showerror(titulo, mensaje)


def crear_tabla_proveedores():
    sql = '''
        CREATE TABLE IF NOT EXISTS proveedores (
            id_proveedores INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL
        );
    '''
    try:
        with conexionDB() as cursor:
            cursor.execute(sql)
    except Exception as e:
        titulo = 'Crear Registro'
        mensaje = f'Error al crear la tabla de proveedores: {e}'
        messagebox.showerror(titulo, mensaje)


def crear_tabla_categorias():
    sql = '''
        CREATE TABLE IF NOT EXISTS categorias (
            id_categorias INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL
        );
    '''
    try:
        with conexionDB() as cursor:
            cursor.execute(sql)
    except Exception as e:
        titulo = 'Crear Registro'
        mensaje = f'Error al crear la tabla de categorías: {e}'
        messagebox.showerror(titulo, mensaje)


def guardar_proveedor(nombre):
    sql = 'INSERT INTO proveedores (nombre) VALUES (?)'
    try:
        with conexionDB() as cursor:
            cursor.execute(sql, (nombre,))
    except Exception as e:
        titulo = 'Guardar Proveedor'
        mensaje = f'Error al guardar el proveedor: {e}'
        messagebox.showerror(titulo, mensaje)


def guardar_categoria(nombre):
    sql = 'INSERT INTO categorias (nombre) VALUES (?)'
    try:
        with conexionDB() as cursor:
            cursor.execute(sql, (nombre,))
    except Exception as e:
        titulo = 'Guardar Categoría'
        mensaje = f'Error al guardar la categoría: {e}'
        messagebox.showerror(titulo, mensaje)


def listar_proveedores():
    sql = 'SELECT nombre FROM proveedores ORDER BY nombre ASC'
    try:
        with conexionDB() as cursor:
            cursor.execute(sql)
            return [row[0] for row in cursor.fetchall()]
    except Exception as e:
        titulo = 'Listar Proveedores'
        mensaje = f'Error al listar los proveedores: {e}'
        messagebox.showerror(titulo, mensaje)
        return []


def listar_categorias():
    sql = 'SELECT nombre FROM categorias ORDER BY nombre ASC'
    try:
        with conexionDB() as cursor:
            cursor.execute(sql)
            return [row[0] for row in cursor.fetchall()]
    except Exception as e:
        titulo = 'Listar Categorías'
        mensaje = f'Error al listar las categorías: {e}'
        messagebox.showerror(titulo, mensaje)
        return []


class Articulos:
    def __init__(self, nombre, proveedor, categoria, precio, stock):
        self.id_articulos = None
        self.nombre = nombre
        self.proveedor = proveedor
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f'Articulos[{self.nombre}, {self.proveedor}, {self.categoria}, {self.precio}, {self.stock}]'


def guardar(articulos):
    sql = '''
        INSERT INTO articulos (nombre, proveedor, categoria, precio, stock)
        VALUES (?, ?, ?, ?, ?)
    '''
    try:
        with conexionDB() as cursor:
            cursor.execute(sql, (articulos.nombre, articulos.proveedor,
                           articulos.categoria, articulos.precio, articulos.stock))
    except Exception as e:
        titulo = 'Conexión al Registro'
        mensaje = f'Error al guardar el artículo: {e}'
        messagebox.showerror(titulo, mensaje)


def listar():
    sql = 'SELECT * FROM articulos ORDER BY id_articulos ASC'
    try:
        with conexionDB() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()
    except Exception as e:
        titulo = 'Listar Registros'
        mensaje = f'Error al listar los artículos: {e}'
        messagebox.showerror(titulo, mensaje)
        return []


def obtener_por_id(articulo_id):
    sql = 'SELECT * FROM articulos WHERE id_articulos = ?'
    try:
        with conexionDB() as cursor:
            cursor.execute(sql, (articulo_id,))
            result = cursor.fetchone()
            if result:
                return Articulos(result[1], result[2], result[3], result[4], result[5])
            return None
    except Exception as e:
        titulo = 'Obtener Artículo'
        mensaje = f'Error al obtener el artículo: {e}'
        messagebox.showerror(titulo, mensaje)
        return None


def actualizar(articulos):
    sql = '''
        UPDATE articulos
        SET nombre = ?, proveedor = ?, categoria = ?, precio = ?, stock = ?
        WHERE id_articulos = ?
    '''
    try:
        with conexionDB() as cursor:
            cursor.execute(sql, (articulos.nombre, articulos.proveedor, articulos.categoria,
                           articulos.precio, articulos.stock, articulos.id_articulos))
    except Exception as e:
        titulo = 'Actualizar Registro'
        mensaje = f'Error al actualizar el artículo: {e}'
        messagebox.showerror(titulo, mensaje)


def eliminar(articulo_id):
    sql = 'DELETE FROM articulos WHERE id_articulos = ?'
    try:
        with conexionDB() as cursor:
            cursor.execute(sql, (articulo_id,))
    except Exception as e:
        titulo = 'Eliminar Registro'
        mensaje = f'Error al eliminar el artículo: {e}'
        messagebox.showerror(titulo, mensaje)


def buscar_por_nombre_o_categoria(termino):
    sql = '''
        SELECT * FROM articulos
        WHERE nombre LIKE ? OR categoria LIKE ?
    '''
    try:
        with conexionDB() as cursor:
            cursor.execute(sql, ('%' + termino + '%', '%' + termino + '%'))
            return cursor.fetchall()
    except Exception as e:
        titulo = 'Buscar Artículos'
        mensaje = f'Error al buscar los artículos: {e}'
        messagebox.showerror(titulo, mensaje)
        return []
