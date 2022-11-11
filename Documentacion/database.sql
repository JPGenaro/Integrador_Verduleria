create database Verduleria;
use Verduleria;

create table Documento(
    id int PRIMARY KEY auto_increment,
    tipo varchar(30),
    numero int
);

create table Cliente(
    id int PRIMARY KEY auto_increment,
    nombre varchar(30),
    apellido varchar(30),
    direccion varchar(100),
    email varchar(80),
    telefono int,
    cuit int,
    id_Documento int,
    constraint id_Documento foreign key (id_Documento) references Documento(id)
);

create table FormaPago(
    id int PRIMARY KEY auto_increment,
    nombre varchar(40),
    descripcion varchar(100)
);

create table Venta(
    id int PRIMARY KEY auto_increment,
    detalle varchar(50),
    fecha date,
    id_FormaPago int,
    id_Cliente int,
    constraint id_FormaPago foreign key (id_FormaPago) references FormaPago(id),
    constraint id_Cliente foreign key (id_Cliente) references Cliente(id)
);

create table TipoProducto(
    id int PRIMARY KEY auto_increment,
    nombre varchar(50),
    descripcion varchar(50)
);

create table Producto(
    id int PRIMARY KEY auto_increment,
    nombre varchar(50),
    precio float,
    stock float,
    id_TipoProducto int,
    constraint id_TipoProducto foreign key (id_TipoProducto) references TipoProducto(id)
);

create table DetalleProductoVenta(
    id int PRIMARY KEY auto_increment,
    precioProducto float,
    cantidadProducto int,
    id_Producto int,
    id_Venta int,
    constraint id_Producto foreign key (id_Producto) references Producto(id),
    constraint id_Venta foreign key (id_Venta) references Venta(id)
);
