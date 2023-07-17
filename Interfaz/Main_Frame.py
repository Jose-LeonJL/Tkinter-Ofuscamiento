import datetime
import tkinter.messagebox
from tkinter import Tk, simpledialog,ttk
import customtkinter
from faker import Faker
import Interfaz.Ui as App
import Interfaz.Login_Frame as LoginView
import Controller.Faker as FakerController
from PIL import Image
import os
import csv

import Models.clientes
import database.database

widgets = []
index_frame_mid_derecha = 0
index_lbl_mid = 1
index_tabla = 15
index_scroll = 16
index_scrolly = 17
combobox_var = customtkinter.StringVar(value="Seleccione")
datoss = []

def configure_interfaz():
    App.app.minsize(1000, 650)
    App.app.maxsize(1000, 650)
    App.app.geometry("1000x650")
    App.app.title("Main")
    App.center_window(App.app, 1000, 650)


def starts():
    configure_interfaz()
    build_frame_main()

    App.app.mainloop()


def addwidget(widget):
    widgets.append(widget)


def destroywidgets():
    for i in widgets:
        i.destroy()



def build_frame_main():
    frame_main = customtkinter.CTkFrame(master=App.app)
    frame_main.pack(side="top", expand=True, fill="both")
    build_frame_derecha(frame_main)
    build_frame_centro(frame_main)
    addwidget(frame_main)


def build_frame_derecha(master):
    frame_izquierda = customtkinter.CTkFrame(master=master)
    frame_izquierda.pack(side="left", expand=True, fill="both")
    frame_izquierda.pack()
    addwidget(frame_izquierda)
    build_frame_derecha_body(frame_izquierda)

def build_frame_centro(master):
    frame_centro = customtkinter.CTkFrame(master=master)
    frame_centro.pack(expand=True, fill="both")
    frame_centro.pack()
    addwidget(frame_centro)

    #agregando los 2 frames para la creacion de datos y exportacion de los mismos
    build_frame_top_derecha(frame_centro)
    build_frame_mid_derecha(frame_centro)
    build_frame_button_derecha(frame_centro)


def build_frame_top_derecha(master):
    frame_top = customtkinter.CTkFrame(master=master, border_width=1, corner_radius=0)
    frame_top.pack(expand=True, fill="both")
    addwidget(frame_top)

    build_frame_top_body(frame_top)


def build_frame_mid_derecha(master):
    frame_mid_derecha = customtkinter.CTkFrame(master=master, border_width=1, corner_radius=0)
    frame_mid_derecha.pack(expand=True, fill="both")
    addwidget(frame_mid_derecha)
    build_frame_mid_body(frame_mid_derecha)


def build_frame_button_derecha(master):
    frame_top = customtkinter.CTkFrame(master=master, border_width=1, corner_radius=0)
    frame_top.pack(expand=True, fill="both")
    addwidget(frame_top)
    build_frame_button_body(frame_top)


def build_frame_top_body(master):
    lblexportar = customtkinter.CTkLabel(master=master, text="Exportar", fg_color="transparent", font=("Sans-Serif", 14),
                                           pady=5)
    boton_exportar = customtkinter.CTkButton(master=master, text="Exportar", height=30,
                                          fg_color="#1E31C3",command=exportfile)
    boton_salir = customtkinter.CTkButton(master=master, text="Salir", height=30,
                                             fg_color="#E52F2F",command=exit)
    lblexportar.pack(expand=True)
    boton_exportar.pack(expand=True)
    boton_salir.pack(expand=True)
    addwidget(lblexportar)
    addwidget(boton_exportar)
    addwidget(boton_salir)


def build_frame_mid_body(master):
    lbl_selectdata = customtkinter.CTkLabel(master=master, text="Seleccione la tabla", fg_color="transparent",
                                            font=("Sans-Serif", 14), pady=5)
    lbl_ = customtkinter.CTkLabel(master=master, text="")
    cbox_tablas = customtkinter.CTkComboBox(master=master, values=["Empleados", "Clientes", "Usuarios"],
                                            command=build_table_frame, variable=combobox_var)
    lbl_selectdata.pack(expand=True)
    cbox_tablas.pack(expand=True)
    lbl_.pack(padx=100)
    addwidget(lbl_selectdata)
    addwidget(lbl_)
    addwidget(cbox_tablas)

def build_frame_button_body(master):
    lblexportar = customtkinter.CTkLabel(master=master, text="Generar datos", fg_color="transparent",
                                         font=("Sans-Serif", 14), pady=5)
    boton_exportar = customtkinter.CTkButton(master=master, text="Generar", height=30,
                                             fg_color="#1E31C3", command=crear_datos)
    lblexportar.pack(expand=True)
    boton_exportar.pack(expand=True)
    addwidget(lblexportar)
    addwidget(boton_exportar)


def crear_datos():
    FakerController.create_registros(10)
    ctk = tkinter.messagebox.showinfo(title="Datos generados",message="Datos ingresados")


def build_frame_derecha_body(master):
    lbl_frame_center = customtkinter.CTkLabel(master=master, text="Seleccione una tabla para visualizar los datos",
                                              fg_color="transparent",
                                              font=("Sans-Serif", 14))
    lbl_frame_center.pack(expand=True, fill="both")
    addwidget(lbl_frame_center)

def build_table_frame(choice):

    if len(widgets) > index_tabla:
        print(len(widgets))
        print(widgets[index_scrolly] is None)
        widgets[index_tabla].destroy()
        widgets[index_scroll].destroy()
        widgets[index_scrolly].destroy()

        widgets.remove(widgets[index_scrolly])
        widgets.remove(widgets[index_scroll])
        widgets.remove(widgets[index_tabla])


    print(len(widgets))

    tree_width = widgets[index_frame_mid_derecha].winfo_width()
    tree_height = widgets[index_frame_mid_derecha].winfo_height()
    #Obtencion de los datos de la tabla, destruccion de LABEL
    widgets[index_lbl_mid].destroy()
    datos = database.database.read_table(choice.lower())
    datoss = datos
    nombres_variables = []

    #OBTENCION DE LOS NOMBRES DE LAS COLUMNAS
    for objeto in datos:
        nombres_variables.extend(objeto.__dict__.keys())
    nombres_variables = list(set(nombres_variables))

    tabla = ttk.Treeview(master=widgets[index_frame_mid_derecha], columns=(nombres_variables),
                         )

    scrollbarx = ttk.Scrollbar(master=widgets[index_frame_mid_derecha], orient="horizontal", command=tabla.xview)
    scrollbary = ttk.Scrollbar(master=widgets[index_frame_mid_derecha], orient="vertical", command=tabla.yview)
    scrollbarx.pack(side="bottom", fill="x")
    scrollbary.pack(side="left", fill="y")
    scrollbarx.place(x=0, y=633, width=798, height=17)

    #scrollbary.place()
    tabla.pack(side="left")
    tabla.configure(xscrollcommand=scrollbarx.set)
    tabla.configure(yscrollcommand=scrollbary.set)
    count= 0

    for _ in nombres_variables:
        tabla.heading(f"#{count}", text=_, anchor="center")
        count += 1

    count = 0
    for _ in datos:
        valuess = []
        primero = 0

        for da in nombres_variables:
            if count == 0:
                primero = getattr(_,da)
                count+=1
            else:
                valuess.append(getattr(_,da))

        tabla.insert("", "end",text=primero, values=valuess)
        count =0

    #Obtener el tamaño del contenido del TreeView
    tabla.update_idletasks()
    tabla.place(x=0, y=0, width=799, height=650)

    #print(f"Tamañox horizon {widgets[index_frame_mid_derecha].winfo_width()}")
    #print(f"Tamañox horizon {scrollbarx.winfo_width()}")
    #print(f"Tamañox vertical {scrollbarx.winfo_height()}")
    #print(f"positionx x {scrollbarx.winfo_x()}")
    #print(f"positionx y {scrollbarx.winfo_y()}")
    #print(f"Tamañoy horizon {scrollbary.winfo_width()}")
    #print(f"Tamañox vertical {scrollbary.winfo_height()}")
    #print(f"positiony x {scrollbary.winfo_x()}")
    #print(f"positionx y {scrollbary.winfo_y()}")
    #print()
    #print()

    addwidget(tabla)
    addwidget(scrollbarx)
    addwidget(scrollbary)

def exportfile():
    # Nombre del archivo CSV a crear
    fecha = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    nombre_archivo = os.path.join(os.path.dirname(os.path.realpath(__file__)), f"{combobox_var.get()}-{fecha}.csv")
    datos = database.database.read_table(combobox_var.get().lower())
    nombres_variables = []

    # OBTENCION DE LOS NOMBRES DE LAS COLUMNAS
    for objeto in datos:
        nombres_variables.extend(objeto.__dict__.keys())
    nombres_variables = list(set(nombres_variables))
    datostoinsert = []
    header = []
    for s in nombres_variables:
        header.append(s)
    datostoinsert.append(header)
    print(1)
    print(nombres_variables)

    for _ in datos:
        valuess = []
        for da in nombres_variables:
            try:

                value = getattr(_,da )
                valuess.append(value)
            except Exception as e:
                e =e
        datostoinsert.append(valuess)
    print(datostoinsert)

    # Escribir los datos en el archivo CSV
    with open(nombre_archivo, "w", newline="") as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerows(datostoinsert)



    ctk = tkinter.messagebox.showinfo(title="Datos exportados", message=f"Se exporto {combobox_var.get()}")

def exit():
    destroywidgets()
    widgets.clear()
    LoginView.starts()
