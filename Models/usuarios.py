from datetime import datetime
import uuid


class Usuarios:
    def __init__(self,usuario_id , nombre, apellido, correo, password,create_at,modify_at):
        self.usuario_id = str(usuario_id)
        self.usuario_nombre = nombre
        self.usuario_apellido = apellido
        self.usuario_correo = correo
        self.usuario_password = password
        self.create_at = create_at
        self.modify_at = modify_at



