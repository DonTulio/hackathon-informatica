from django.db import models

class Alumno(models.Model):
    alumnoid = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apaterno = models.CharField(max_length=20)
    amaterno = models.CharField(max_length=20)
    genero = models.CharField(max_length=1, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    carreraid = models.ForeignKey('Carrera', models.DO_NOTHING, db_column='carreraid')

    class Meta:
        managed = False
        db_table = 'alumno'


class Autor(models.Model):
    tituloid = models.OneToOneField('Titulo', models.DO_NOTHING, db_column='tituloid', primary_key=True,related_name='autor_tituloid')
    autorid = models.IntegerField()
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'autor'
        unique_together = (('tituloid', 'autorid'),)


class Carrera(models.Model):
    carreraid = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    escuelaid = models.ForeignKey('Escuela', models.DO_NOTHING, db_column='escuelaid')

    class Meta:
        managed = False
        db_table = 'carrera'


class Editorial(models.Model):
    editorialid = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'editorial'


class Ejemplar(models.Model):
    tituloid = models.ForeignKey('Titulo', models.DO_NOTHING, db_column='tituloid' ,related_name='ejemplar_tituloid')
    ejemplarid = models.CharField(primary_key=True, max_length=4)
    isbn = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'ejemplar'
        unique_together = (('ejemplarid', 'tituloid'),)


class Empleado(models.Model):
    empleadoid = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apaterno = models.CharField(max_length=20)
    amaterno = models.CharField(max_length=20)
    fecha_contrato = models.DateField()
    salario = models.IntegerField()
    jefeid = models.ForeignKey('self', models.DO_NOTHING, db_column='jefeid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado'


class Errores(models.Model):
    id_error = models.IntegerField(primary_key=True)
    subprograma_error = models.CharField(max_length=50)
    descripcion_error = models.CharField(max_length=500, blank=True, null=True)
    ocurrencia = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'errores'


class Escuela(models.Model):
    escuelaid = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'escuela'


class PorcMultaPrestamo(models.Model):
    cant_dias_ini = models.IntegerField(primary_key=True)
    cant_dias_ter = models.IntegerField()
    porcentaje_multa = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'porc_multa_prestamo'


class Prestamo(models.Model):
    prestamoid = models.IntegerField(primary_key=True)
    fecha_inicio = models.DateField()
    hora_inicio = models.CharField(max_length=5)
    fecha_termino = models.DateField()
    hora_termino = models.CharField(max_length=5)
    fecha_entrega = models.DateField(blank=True, null=True)
    hora_entrega = models.CharField(max_length=5, blank=True, null=True)
    multa = models.IntegerField(blank=True, null=True)
    glosa_multa = models.CharField(max_length=100, blank=True, null=True)
    tituloid = models.ForeignKey(Ejemplar, models.DO_NOTHING, db_column='tituloid',related_name='topic_tituloid')
    ejemplarid = models.ForeignKey(Ejemplar, models.DO_NOTHING, db_column='ejemplarid',related_name='topic_ejemplarid')
    alumnoid = models.ForeignKey(Alumno, models.DO_NOTHING, db_column='alumnoid')
    empleadoid = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleadoid')

    class Meta:
        managed = False
        db_table = 'prestamo'


class PrestamosLibrosMensuales(models.Model):
    correlativo = models.IntegerField(primary_key=True)
    fecha_proceso = models.CharField(max_length=7)
    libro = models.CharField(max_length=100)
    editorial = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    alumno = models.CharField(max_length=100)
    escuela = models.CharField(max_length=100)
    carrera = models.CharField(max_length=100)
    responble_prest_devol = models.CharField(max_length=100)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField()
    fecha_devolucion_alumno = models.DateField()
    dias_atraso_devolucion = models.IntegerField()
    valor_multa = models.IntegerField(blank=True, null=True)
    fecha_grabacion = models.DateField()

    class Meta:
        managed = False
        db_table = 'prestamos_libros_mensuales'
        unique_together = (('correlativo', 'fecha_proceso'),)


class Titulo(models.Model):
    tituloid = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=70)
    publicacion = models.IntegerField()
    paginas = models.IntegerField()
    precio = models.IntegerField(blank=True, null=True)
    editorialid = models.ForeignKey(Editorial, models.DO_NOTHING, db_column='editorialid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'titulo'
