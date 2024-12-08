
import tkinter as tk
from tkinter import ttk, messagebox
from model.articulos_dao import Articulos, crear_tabla, borrar_tabla, guardar, listar, obtener_por_id, actualizar, eliminar, buscar_por_nombre_o_categoria, listar_proveedores, guardar_proveedor, crear_tabla_proveedores, listar_categorias, guardar_categoria, crear_tabla_categorias


def barra_menu(root, app):
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu, width=300, height=300)

    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Inicio', menu=menu_inicio)

    menu_inicio.add_command(label='Crear registro en DB', command=crear_tabla)
    menu_inicio.add_command(
        label='Eliminar registro en DB', command=borrar_tabla)
    menu_inicio.add_command(label='Salir', command=root.quit)

    menu_consultas = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Consultas', menu=menu_consultas)
    menu_consultas.add_command(
        label='Buscar por Nombre o Categoría', command=lambda: abrir_ventana_busqueda(app))
    menu_consultas.add_command(
        label='Ver Todos los Registros', command=app.actualizar_tabla_articles)

    barra_menu.add_cascade(label='Configuración')
    menu_ayuda = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Ayuda', menu=menu_ayuda)

    menu_contactanos = tk.Menu(menu_ayuda, tearoff=0)
    menu_ayuda.add_cascade(label='Contáctanos', menu=menu_contactanos)

    menu_contactanos.add_command(label='Correo Electrónico', command=lambda: messagebox.showinfo(
        "Contáctanos", "fercormayorista@gmail.com"))
    menu_contactanos.add_command(
        label='Teléfono', command=lambda: messagebox.showinfo("Contáctanos", "011-5245858"))


def abrir_ventana_busqueda(app):
    ventana_busqueda = tk.Toplevel()
    ventana_busqueda.title("Buscar Artículo")
    ventana_busqueda.geometry("300x150")

    label_busqueda = tk.Label(
        ventana_busqueda, text="Ingrese el nombre o categoría del artículo:")
    label_busqueda.pack(pady=10)

    entry_busqueda = tk.Entry(ventana_busqueda, width=30)
    entry_busqueda.pack(pady=10)

    def realizar_busqueda():
        termino_busqueda = entry_busqueda.get()
        resultados = buscar_por_nombre_o_categoria(termino_busqueda)
        if resultados:
            app.mostrar_resultados_busqueda(resultados)
        else:
            messagebox.showinfo("Búsqueda", "No se encontraron resultados.")
        ventana_busqueda.destroy()

    boton_buscar = tk.Button(
        ventana_busqueda, text="Buscar", command=realizar_busqueda)
    boton_buscar.pack(pady=10)


class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()
        self.campos_articulos()
        self.deshabilitar_campos()
        self.crear_tabla_articles()
        self.actualizar_tabla_articles()

    def campos_articulos(self):
        self.label_titulo = tk.Label(self, text='Sistema Carga Productos', font=(
            'Arial', 16, 'bold underline'), bg='#e0e0e0')
        self.label_titulo.grid(row=0, column=0, columnspan=2, pady=10)

        self.label_nombre = tk.Label(self, text='Nombre: ')
        self.label_nombre.config(font=('Arial', 12, 'bold'), bg='#e0e0e0')
        self.label_nombre.grid(row=1, column=0, padx=10, pady=10, sticky='e')

        self.label_proveedor = tk.Label(self, text='Proveedor: ')
        self.label_proveedor.config(font=('Arial', 12, 'bold'), bg='#e0e0e0')
        self.label_proveedor.grid(
            row=2, column=0, padx=10, pady=10, sticky='e')
        self.label_categoria = tk.Label(self, text='Categoría: ')
        self.label_categoria.config(font=('Arial', 12, 'bold'), bg='#f0f0f0')
        self.label_categoria.grid(
            row=3, column=0, padx=10, pady=10, sticky='e')

        self.label_precio = tk.Label(self, text='Precio: ')
        self.label_precio.config(font=('Arial', 12, 'bold'), bg='#f0f0f0')
        self.label_precio.grid(row=4, column=0, padx=10, pady=10, sticky='e')

        self.label_stock = tk.Label(self, text='Stock: ')
        self.label_stock.config(font=('Arial', 12, 'bold'), bg='#f0f0f0')
        self.label_stock.grid(row=5, column=0, padx=10, pady=10, sticky='e')

        self.mi_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable=self.mi_nombre)
        self.entry_nombre.config(
            width=50, state='disabled', font=('Arial', 12))
        self.entry_nombre.grid(row=1, column=1, padx=10, pady=10)

        self.mi_proveedor = tk.StringVar()
        self.select_proveedor = ttk.Combobox(
            self, textvariable=self.mi_proveedor)
        self.select_proveedor.config(
            width=47, state='disabled', font=('Arial', 12))
        self.select_proveedor['values'] = listar_proveedores()
        self.select_proveedor.grid(row=2, column=1, padx=10, pady=10)

        self.mi_categoria = tk.StringVar()
        self.select_categoria = ttk.Combobox(
            self, textvariable=self.mi_categoria)
        self.select_categoria.config(
            width=47, state='disabled', font=('Arial', 12))
        self.select_categoria['values'] = listar_categorias()
        self.select_categoria.grid(row=3, column=1, padx=10, pady=10)

        self.mi_precio = tk.StringVar()
        self.entry_precio = tk.Entry(self, textvariable=self.mi_precio)
        self.entry_precio.config(
            width=50, state='disabled', font=('Arial', 12))
        self.entry_precio.grid(row=4, column=1, padx=10, pady=10)

        self.mi_stock_check = tk.BooleanVar()
        self.check_stock = tk.Checkbutton(
            self, text='En Stock', variable=self.mi_stock_check, state='disabled', command=self.toggle_stock_entry)
        self.check_stock.config(font=('Arial', 12), bg='#f0f0f0')
        self.check_stock.grid(row=5, column=1, padx=10, pady=10, sticky='w')

        self.mi_stock_entry = tk.StringVar()
        self.entry_stock = tk.Entry(self, textvariable=self.mi_stock_entry)
        self.entry_stock.config(width=10, state='disabled', font=(
            'Arial', 12), justify='center')
        self.entry_stock.grid(row=5, column=1, padx=10, pady=10, sticky='e')

        self.boton_nuevo = tk.Button(
            self, text="Nuevo", command=self.habilitar_campos)
        self.boton_nuevo.config(width=20, font=(
            'Arial', 12, 'bold'), fg='#DAD5D6', bg='#158645', cursor='hand2', activebackground='#35BD6F')
        self.boton_nuevo.grid(row=6, column=0, padx=10, pady=10)

        self.boton_guardar = tk.Button(
            self, text="Guardar", command=self.guardar_datos)
        self.boton_guardar.config(width=20, font=(
            'Arial', 12, 'bold'), fg='#DAD5D6', bg='#1658A2', cursor='hand2', activebackground='#3586DF')
        self.boton_guardar.grid(row=6, column=1, padx=10, pady=10)

        self.boton_cancelar = tk.Button(
            self, text="Cancelar", command=self.deshabilitar_campos)
        self.boton_cancelar.config(width=20, font=(
            'Arial', 12, 'bold'), fg='#DAD5D6', bg='#bd152E', cursor='hand2', activebackground='#E15370')
        self.boton_cancelar.grid(row=6, column=2, padx=10, pady=10)

    def toggle_stock_entry(self):
        if self.mi_stock_check.get():
            self.entry_stock.config(state='normal')
        else:
            self.entry_stock.config(state='disabled')
            self.mi_stock_entry.set('')

    def habilitar_campos(self):
        self.mi_nombre.set('')
        self.mi_proveedor.set('')
        self.mi_categoria.set('')
        self.mi_precio.set('')
        self.mi_stock_check.set(False)
        self.mi_stock_entry.set('')

        self.entry_nombre.config(state='normal')
        self.select_proveedor.config(state='normal')
        self.select_categoria.config(state='normal')
        self.entry_precio.config(state='normal')
        self.check_stock.config(state='normal')
        self.entry_stock.config(state='disabled')

        self.boton_guardar.config(state='normal')
        self.boton_cancelar.config(state='normal')

    def deshabilitar_campos(self):
        self.mi_nombre.set('')
        self.mi_proveedor.set('')
        self.mi_categoria.set('')
        self.mi_precio.set('')
        self.mi_stock_check.set(False)
        self.mi_stock_entry.set('')

        self.entry_nombre.config(state='disabled')
        self.select_proveedor.config(state='disabled')
        self.select_categoria.config(state='disabled')
        self.entry_precio.config(state='disabled')
        self.check_stock.config(state='disabled')
        self.entry_stock.config(state='disabled')

        self.boton_guardar.config(state='disabled')
        self.boton_cancelar.config(state='disabled')

    def guardar_datos(self):
        proveedor = self.mi_proveedor.get()
        if proveedor not in listar_proveedores():
            guardar_proveedor(proveedor)
            self.select_proveedor['values'] = listar_proveedores()

        categoria = self.mi_categoria.get()
        if categoria not in listar_categorias():
            guardar_categoria(categoria)
            self.select_categoria['values'] = listar_categorias()

        stock = self.mi_stock_entry.get() if self.mi_stock_check.get() else 0
        articulos = Articulos(
            self.mi_nombre.get(),
            self.mi_proveedor.get(),
            self.mi_categoria.get(),
            self.mi_precio.get(),
            stock
        )
        selected_item = self.tabla.selection()
        if selected_item:
            item = self.tabla.item(selected_item)
            articulos.id_articulos = item['text']
            actualizar(articulos)
        else:
            guardar(articulos)
        self.deshabilitar_campos()
        self.actualizar_tabla_articles()

    def editar_datos(self):
        selected_item = self.tabla.selection()
        if not selected_item:
            return

        item = self.tabla.item(selected_item)
        articulo_id = item['text']
        articulo = obtener_por_id(articulo_id)

        if articulo:
            self.mi_nombre.set(articulo.nombre)
            self.mi_proveedor.set(articulo.proveedor)
            self.mi_categoria.set(articulo.categoria)
            self.mi_precio.set(articulo.precio)
            self.mi_stock_check.set(articulo.stock > 0)
            self.mi_stock_entry.set(
                articulo.stock if articulo.stock > 0 else '')

            self.entry_nombre.config(state='normal')
            self.select_proveedor.config(state='normal')
            self.select_categoria.config(state='normal')
            self.entry_precio.config(state='normal')
            self.check_stock.config(state='normal')
            self.entry_stock.config(
                state='normal' if articulo.stock > 0 else 'disabled')

            self.boton_guardar.config(state='normal')
            self.boton_cancelar.config(state='normal')

    def eliminar_datos(self):
        try:
            self.id_articulos = self.tabla.item(self.tabla.selection())['text']
            eliminar(self.id_articulos)
            self.actualizar_tabla_articles()
        except:
            titulo = 'Eliminar un registro'
            mensaje = 'No ha seleccionado ningún registro'
            messagebox.showerror(titulo, mensaje)

    def crear_tabla_articles(self):
        style = ttk.Style()
        style.configure("Treeview", background="lightblue",
                        fieldbackground="lightblue", foreground="black")
        style.map("Treeview", background=[("selected", "darkblue")])

        self.tabla = ttk.Treeview(self, columns=(
            'Nombre', 'Proveedor', 'Categoria', 'Precio', 'Stock'), style="Treeview")
        self.tabla.grid(row=7, column=0, columnspan=5, sticky='nsew', padx=28)

        self.scroll = ttk.Scrollbar(
            self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=7, column=5, sticky='ns', padx=(0, 28))
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.column('#0', width=50, anchor='center')
        self.tabla.column('Nombre', width=150, anchor='center')
        self.tabla.column('Proveedor', width=150, anchor='center')
        self.tabla.column('Categoria', width=150, anchor='center')
        self.tabla.column('Precio', width=100, anchor='center')
        self.tabla.column('Stock', width=100, anchor='center')

        self.tabla.heading('#0', text='id')
        self.tabla.heading('Nombre', text='Nombre')
        self.tabla.heading('Proveedor', text='Proveedor')
        self.tabla.heading('Categoria', text='Categoría')
        self.tabla.heading('Precio', text='Precio')
        self.tabla.heading('Stock', text='Stock')

        button_frame = tk.Frame(self)
        button_frame.grid(row=8, column=0, columnspan=6, pady=10)

        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)

        self.boton_editar = tk.Button(
            button_frame, text="Editar", command=self.editar_datos)
        self.boton_editar.config(width=20, font=(
            'Arial', 12, 'bold'), fg='#DAD5D6', bg='#158645', cursor='hand2', activebackground='#35BD6F')
        self.boton_editar.grid(row=0, column=0, padx=10)

        self.boton_eliminar = tk.Button(
            button_frame, text="Eliminar", command=self.eliminar_datos)
        self.boton_eliminar.config(width=20, font=(
            'Arial', 12, 'bold'), fg='#DAD5D6', bg='#bd152E', cursor='hand2', activebackground='#E15370')
        self.boton_eliminar.grid(row=0, column=1, padx=10)

    def actualizar_tabla_articles(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        self.lista_articulos = listar()

        for p in self.lista_articulos:
            self.tabla.insert('', 'end', text=p[0], values=(
                p[1], p[2], p[3], p[4], p[5]))

    def mostrar_resultados_busqueda(self, resultados):
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        for p in resultados:
            self.tabla.insert('', 'end', text=p[0], values=(
                p[1], p[2], p[3], p[4], p[5]))


def main():
    root = tk.Tk()
    root.title('Catálogo de Artículos para Ferreterías')
    root.iconbitmap('img/fcm.ico')
    root.resizable(0, 0)

    style = ttk.Style()
    style.configure("TFrame", background="#f0f0f0")
    style.configure("TLabel", background="#f0f0f0", font=("Helvetica", 12))
    style.configure("TButton", background="#4CAF50",
                    foreground="white", font=("Helvetica", 12))
    style.map("TButton", background=[("active", "#45a049")])

    # Crear las tablas al inicio de la aplicación
    crear_tabla()
    crear_tabla_proveedores()
    crear_tabla_categorias()

    app = Frame(root=root)
    barra_menu(root, app)

    root.configure(bg="#f0f0f0")

    root.mainloop()


if __name__ == '__main__':
    main()
