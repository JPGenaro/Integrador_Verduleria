# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=30, blank=True, null=True)
    apellido = models.CharField(max_length=30, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=80, blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)
    cuit = models.IntegerField(blank=True, null=True)
    id_documento = models.ForeignKey('Documento', models.DO_NOTHING, db_column='id_Documento', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cliente'
    
    def __str__(self) -> str:
        return f'{self.apellido}, {self.nombre}'


class Detalleproductoventa(models.Model):
    precioproducto = models.FloatField(db_column='precioProducto', blank=True, null=True)  # Field name made lowercase.
    cantidadproducto = models.IntegerField(db_column='cantidadProducto', blank=True, null=True)  # Field name made lowercase.
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_Producto', blank=True, null=True)  # Field name made lowercase.
    id_venta = models.ForeignKey('Venta', models.DO_NOTHING, db_column='id_Venta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DetalleProductoVenta'
    
    def __str__(self) -> str:
        return f'ID Producto: {self.id_producto}, ID Venta: {self.id_venta}'


class Documento(models.Model):
    tipo = models.CharField(max_length=30, blank=True, null=True)
    numero = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Documento'
    
    def __str__(self) -> str:
        return f'N° {self.numero}'


class Formapago(models.Model):
    nombre = models.CharField(max_length=40, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FormaPago'
    
    def __str__(self) -> str:
        return str(self.nombre)


class Producto(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)
    stock = models.FloatField(blank=True, null=True)
    id_tipoproducto = models.ForeignKey('Tipoproducto', models.DO_NOTHING, db_column='id_TipoProducto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Producto'
    
    def __str__(self) -> str:
        return f'{self.nombre} ({self.id_tipoproducto}), ${self.precio}'


class Tipoproducto(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TipoProducto'
    
    def __str__(self) -> str:
        return str(self.nombre)


class Venta(models.Model):
    detalle = models.CharField(max_length=50, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    id_formapago = models.ForeignKey(Formapago, models.DO_NOTHING, db_column='id_FormaPago', blank=True, null=True)  # Field name made lowercase.
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_Cliente', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Venta'
    
    def __str__(self) -> str:
        return f'Cliente: {self.id_cliente}, Fecha: {self.fecha}'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
