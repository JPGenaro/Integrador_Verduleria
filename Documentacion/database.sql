create database Verduleria;
use Verduleria;

create table Documento(
    id int PRIMARY KEY auto_increment,
    tipo varchar(30),
    numero varchar(45)
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

#Datos a usar...

insert into Documento values(1, "DNI", "25462548");
insert into Documento values(2, "CI", "12754654-K");
insert into Documento values(3, "CC", "11001010101");
insert into Documento values(4, "CURP", "MSDJ025541SFKRKFR78");

insert into TipoProducto values(1, "Frutas", "");
insert into TipoProducto values(2, "Verduras", "");
insert into TipoProducto values(3, "Especias", "");
insert into TipoProducto values(4, "Otros", "");

insert into Producto values(1, "Manzana", 400, 50, 1);
insert into Producto values(2, "Peras", 350, 50, 1);
insert into Producto values(3, "Naranjas", 420, 80, 1);
insert into Producto values(4, "Limon", 200, 120, 1);
insert into Producto values(5, "Kiwi", 600, 40, 1);
insert into Producto values(6, "Tomate", 350, 60, 1);

insert into Producto values(7, "Pimenton", 220, 50, 2);
insert into Producto values(8, "Papas", 320, 150, 2);
insert into Producto values(9, "Lechuga", 280, 90, 2);
insert into Producto values(10, "Cebolla", 190, 60, 2);
insert into Producto values(11, "Zanahoria", 310, 75, 2);
insert into Producto values(12, "Calabaza", 550, 30, 2);

insert into Producto values(13, "Canela", 80, 50, 3);
insert into Producto values(14, "Paprica", 90, 50, 3);
insert into Producto values(15, "Pimenton Dulce", 120, 50, 3);
insert into Producto values(16, "Laurel", 60, 50, 3);
insert into Producto values(17, "Oregano", 80, 50, 3);
insert into Producto values(18, "Romero", 85, 60, 3);

insert into Producto values(19, "Huevos", 300, 150, 4);
insert into Producto values(20, "Miel", 360, 95, 4);
insert into Producto values(21, "Champiñon", 295, 80, 4);
insert into Producto values(22, "Arandanos", 50, 20, 4);

insert into FormaPago values(1, "Efectivo", "Pago en persona");
insert into FormaPago values(2, "Tarjeta debito", "");
insert into FormaPago values(3, "Tarjeta credito", "");
insert into FormaPago values(4, "Transferencia", "Mercado libre, etc");

insert into Cliente values(1, "Lisandro", "Marquez",  "Soldado Ramon Cabrera 6855", "lichiMarquez@gmail.com", 3512246, 65651651, 1);

