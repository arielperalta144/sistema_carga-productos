Trabajo integrador Python
Sistema de Carga de Productos
Descripción
Este proyecto es un sistema de gestión de productos para ferreterías. Permite a los usuarios agregar, editar, eliminar y buscar productos en una base de datos. Además, maneja categorías y proveedores de productos.
Caracteristicas
•	Gestión de Productos : Agregar, editar, eliminar y buscar productos.
•	Gestión de Categorías : Agregar y listar categorías de productos.
•	Gestión de Proveedores : Agregar y listar proveedores de productos.
•	Interfaz Gráfica : Interfaz gráfica intuitiva y elegante para una mejor experiencia de usuario.
Requisitos
•	Python 3.2
•	SQLite (incluido con Python)
•	Tkinter (incluido con Python)
Instalación
1.	Clonar el repositorio :
https://github.com/arielperalta144/sistema_carga-productos.git
2.Instalar Dependencias: No se requieren dependencias adicionales, ya que el proyecto utiliza bibliotecas estándar de Python.
3.	Ejecutar la aplicación : a) crear un entorno virtual env\scripts\activate b) ingresar al directorio / cd Catalogo_ferreteria c) ejecutar el programa python main.py
ejemplo : PS C:\Users\ariel\Desktop\CRUD> env\scripts\activate (env) PS C:\Users\ariel\Desktop\CRUD> cd catalogo_ferreteria\python main.py
Uso Agregar un producto:
Ingrese los detalles del producto en los campos correspondientes. Seleccione el proveedor y la categoría del producto. Haga clic en el botón "Guardar". Editar un Producto:
Seleccione el producto que desea editar en la tabla. Modifique los detalles del producto en los campos correspondientes. Haga clic en el botón "Guardar". Eliminar un Producto:
Seleccione el producto que desea eliminar en la tabla. Haga clic en el botón "Eliminar". Buscar un Producto:
Haga clic en "Consultas" en el menú y seleccione "Buscar por Nombre o Categoría". Ingrese el nombre o categoría del producto en la ventana emergente. Haga clic en "Buscar". Agregar una categoría o proveedor:
Ingrese el nombre de la categoría o proveedor en el campo correspondiente.
Si la categoría o proveedor no existe, se agregará automáticamente al guardar el producto.
Estructura del proyecto
model/articulos_dao.py: Contiene las funciones para interactuar con la base de datos. main.py: Contiene la interfaz gráfica y la lógica principal de la aplicación. conexion_db.py: Contiene la configuración de la conexión a la base de datos.
