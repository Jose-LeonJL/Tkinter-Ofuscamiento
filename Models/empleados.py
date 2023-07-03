import uuid


class Empleados:
    def __init__(self,empleado_id, identidad, numero_telefonico, nombre, direccion, salario):
        self.empleado_id = str(empleado_id)
        self.empleado_identidad = identidad
        self.empleado_numero_telefonico = numero_telefonico
        self.empleado_nombre = nombre
        self.empleado_direccion = direccion
        self.empleado_salario = salario
