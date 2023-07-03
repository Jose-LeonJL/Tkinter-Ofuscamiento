import uuid

from faker import Faker
from Models.usuarios import Usuarios
from database.database import bulk_create,read_table
from Models.empleados import Empleados
from Models.clientes import Clientes
from datetime import datetime

def create_registros(cantidad):
    faker = Faker()
    usuarios_lista = []
    clientes_lista = []
    empleados_lista = []

    for _ in range(cantidad):
        usuarios_lista.append(Usuarios(usuario_id=uuid.uuid4(),nombre=faker.name(), password=faker.password(),
                                       apellido=faker.name(), correo=faker.email(),
                                       create_at=datetime.now(), modify_at=datetime.now()))
        empleados_lista.append(Empleados(empleado_id=uuid.uuid4(),identidad=faker.unique.random_number(digits=15),
                                         nombre=faker.name(), direccion=faker.address(),
                                         numero_telefonico=faker.numerify(text='########'),
                                         salario=faker.random_number(digits=8)))
        clientes_lista.append(Clientes(cliente_id=uuid.uuid4(),cuenta_bancaria=faker.unique.random_number(digits=15),
                                       identidad=faker.unique.random_number(digits=15),
                                       numero_telefonico=faker.unique.random_number(digits=8),
                                       nombre=faker.name(), direccion=faker.address(),
                                       numero_tarjeta_credito=faker.unique.random_number(digits=12), cliente_fecha_nacimiento=datetime.now()))
    bulk_create("usuarios", usuarios_lista)
    bulk_create("clientes", clientes_lista)
    bulk_create("empleados", empleados_lista)
