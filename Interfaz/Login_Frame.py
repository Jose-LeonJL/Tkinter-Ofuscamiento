import customtkinter
import Interfaz.Main_Frame as Main
import Interfaz.Ui as App
from PIL import Image
import os
import tkinter.messagebox as messagebox
import re

widgets = []

def configure_interfaz():
    App.app.minsize(450, 650)
    App.app.maxsize(450, 650)
    App.app.geometry("450x650")
    App.app.title("Login")
    App.center_window(App.app, 450, 650)


def starts():
    configure_interfaz()
    insert_icon()
    insert_types()
    App.app.mainloop()


def insert_icon():
    imagen_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "src")
    image_icon = customtkinter.CTkImage(light_image=Image.open(os.path.join(imagen_path, "ico.png")),
                                        dark_image=Image.open(os.path.join(imagen_path, "ico.png")),
                                        size=(120, 120))
    image_label = customtkinter.CTkLabel(master=App.app, image=image_icon,
                                         text="", width=450)
    image_label.pack(pady=30)
    addwidget(image_label)

def insert_types():
    global text_password
    global text_usuario
    label_inicie_session = customtkinter.CTkLabel(master=App.app, text="Inicie Sesion",
                                                  fg_color="transparent", font=("Sans-Serif", 20),
                                                  width=450)
    lblpaddyn = customtkinter.CTkLabel(master=App.app, text="", fg_color="transparent", height=45)
    label_usuario = customtkinter.CTkLabel(master=App.app, text="Ingrese su usuario", fg_color="transparent", font=("Sans-Serif", 14),
                                           pady=5)
    text_usuario = customtkinter.CTkTextbox(master=App.app, corner_radius=5, border_width=1,
                                          height=15, width=225)
    label_password = customtkinter.CTkLabel(master=App.app, text="Ingrese su contraseña",
                                            fg_color="transparent", font=("Sans-Serif", 14),
                                            pady=5)
    text_password = customtkinter.CTkTextbox(master=App.app, corner_radius=5, border_width=1,
                                             height=15, width=225)
    boton_login = customtkinter.CTkButton(master=App.app, text="Login", width=225, height=30,
                                          fg_color="#1E31C3",command=boton_event_login)

    label_inicie_session.pack(pady=10)
    lblpaddyn.pack()
    label_usuario.pack(pady=5)
    text_usuario.pack(pady=0)
    label_password.pack(pady=5)
    text_password.pack(pady=0)
    boton_login.pack(pady=25)
    addwidget(label_inicie_session)
    addwidget(lblpaddyn)
    addwidget(label_usuario)
    addwidget(text_usuario)
    addwidget(label_password)
    addwidget(text_password)
    addwidget(boton_login)


def addwidget(widget):
    widgets.append(widget)


def destroywidgets():
    for i in widgets:
        i.destroy()


def boton_event_login():
    global text_password
    global text_usuario

    usuario = text_usuario.get("1.0", "end-1c")
    contraseña = text_password.get("1.0", "end-1c")

    text_usuario.delete("1.0", "end")
    text_password.delete("1.0", "end")

    mensaje_error = validar_credenciales(usuario, contraseña)

    # Verificar las credenciales
    if mensaje_error == 0:
     messagebox.showinfo("Inicio de sesión exitoso", "¡Bienvenido(a)!")
     destroywidgets()
     widgets.clear()
     Main.starts()
    elif mensaje_error == 1:
        messagebox.showerror("Error de inicio de sesión", "El usuario debe tener al menos 5 caracteres.")
    elif mensaje_error == 2:
        messagebox.showerror("Error de inicio de sesión", "La contraseña debe tener al menos 8 caracteres.")
    elif mensaje_error == 3:
        messagebox.showerror("Error de inicio de sesión", "El usuario solo puede contener letras y números no se permiten espacios.")
    elif mensaje_error == 4:
        messagebox.showerror("Error de inicio de sesión",
                         "La contraseña debe contener al menos una letra minúscula, una letra mayúscula, un digito y un caracter especial!.")
    else:
        messagebox.showerror("Error de inicio de sesión", "Usuario/Contraseña inválidos.")

def validar_credenciales(usuario, contraseña):
            # Verificar si el usuario y la contraseña cumplen con los requisitos
            if len(usuario) < 5:
                return 1
            if len(contraseña) < 8:
                return 2

            # Verificar si el usuario contiene solo letras y números
            if not re.match("^[a-zA-Z0-9]+$", usuario):
                return 3

            # Verificar si la contraseña contiene al menos una letra minúscula, una letra mayúscula, un dígito y caracter especial!
            if not (re.search("[a-z]", contraseña) and re.search("[A-Z]", contraseña) and re.search("[0-9]", contraseña) and re.search("[.]", contraseña)):
                return 4

            if usuario == "admin" and contraseña == "Seguridad.2023":
                return 0

            return 5