create table usuarios(
    usuario_id char(36) primary key,
    usuario_nombre varchar(20) not null,
    usuario_apellido varchar(20) not null,
    usuario_correo varchar(20) not null,
    usuario_password varchar(20) not null,
    create_at datetime,
    modify_at datetime
);

create table clientes(
    cliente_id char(36) primary key,
    cliente_cuenta_bancaria varchar(20) not null,
    cliente_identidad varchar(20) not null,
    cliente_numero_tarjeta_credito varchar(20) not null,
    cliente_numero_telefonico varchar(20) not null,
    cliente_nombre varchar(20) not null,
    cliente_direccion varchar(20) not null,
    cliente_fecha_nacimiento datetime
);

create table empleados(
    empleado_id char(36) primary key,
    empleado_identidad varchar(20) not null,
    empleado_numero_telefonico varchar(20) not null,
    empleado_nombre varchar(20) not null,
    empleado_direccion varchar(20) not null,
    empleado_salario varchar(20) not null
);