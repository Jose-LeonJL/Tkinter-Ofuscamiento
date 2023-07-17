import uuid
from datetime import datetime

class Clientes:
    def __init__(self,cliente_id, cuenta_bancaria, identidad, numero_tarjeta_credito, numero_telefonico, nombre, direccion,cliente_fecha_nacimiento):
        self.cliente_id = str(cliente_id)
        self.cliente_cuenta_bancaria = cuenta_bancaria
        self.cliente_identidad = identidad
        self.cliente_numero_tarjeta_credito = numero_tarjeta_credito
        self.cliente_numero_telefonico = numero_telefonico
        self.cliente_nombre = nombre
        self.cliente_direccion = direccion
        self.cliente_fecha_nacimiento = cliente_fecha_nacimiento
