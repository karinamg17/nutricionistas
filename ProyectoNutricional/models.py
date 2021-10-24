# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Actividadfisica(models.Model):
    idactividadfisica = models.AutoField(primary_key=True)
    realizaejercicio = models.CharField(max_length=1, blank=True, null=True)
    fechaingreso = models.DateField(blank=True, null=True)
    ligera = models.CharField(max_length=1, blank=True, null=True)
    muyligera = models.CharField(max_length=1, blank=True, null=True)
    moderada = models.CharField(max_length=1, blank=True, null=True)
    pesada = models.CharField(max_length=1, blank=True, null=True)
    exhaustiva = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actividadfisica'


class Alimento(models.Model):
    idalimento = models.AutoField(primary_key=True)
    nombrealimento = models.CharField(max_length=800)
    categoria = models.CharField(max_length=800)

    class Meta:
        managed = False
        db_table = 'alimento'


class Aspectosginecologicos(models.Model):
    idginecologico = models.AutoField(primary_key=True)
    anticonceptipos = models.CharField(max_length=1, blank=True, null=True)
    anticoncepdescrip = models.CharField(max_length=800, blank=True, null=True)
    embarazadoactual = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aspectosginecologicos'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Calculonutrientes(models.Model):
    idcalculon = models.AutoField(primary_key=True)
    peso = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    kcalvet = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calculonutrientes'


class Citas(models.Model):
    idcita = models.AutoField(primary_key=True)
    idusuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='idusuario')
    nombre = models.CharField(max_length=800)
    primerapellido = models.CharField(max_length=800)
    fechacita = models.DateField()
    horacita = models.TimeField()
    asunto = models.CharField(max_length=800)

    class Meta:
        managed = False
        db_table = 'citas'


class Comidasrealizadas(models.Model):
    idcomidas = models.AutoField(primary_key=True)
    desayuno = models.CharField(max_length=1, blank=True, null=True)
    meriendamanana = models.CharField(max_length=1, blank=True, null=True)
    almuerzo = models.CharField(max_length=1, blank=True, null=True)
    meriendatarde = models.CharField(max_length=1, blank=True, null=True)
    cena = models.CharField(max_length=1, blank=True, null=True)
    colacionnocturna = models.CharField(max_length=1, blank=True, null=True)
    otro = models.CharField(max_length=800, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comidasrealizadas'


class Consumopreparacionesmedicas(models.Model):
    idconsumo = models.AutoField(primary_key=True)
    laxantes = models.CharField(max_length=1, blank=True, null=True)
    diureticos = models.CharField(max_length=1, blank=True, null=True)
    antiacidos = models.CharField(max_length=1, blank=True, null=True)
    analgesicos = models.CharField(max_length=1, blank=True, null=True)
    vitaminas = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consumopreparacionesmedicas'


class Datosantropometricos(models.Model):
    iddatos = models.AutoField(primary_key=True)
    fecha = models.DateField()
    peso = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pesorecomendado = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    talla = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    imc_kg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    porcgrasa = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    porcmuscesqueletico = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tmb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    edadmetabolica = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    grasavisceral = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    masagrasa_kg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mlg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    masagrasaporcentaje = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    masamuscular_kg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    masamuscularporcentaje = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    masaresidual_kg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    masaresidualporcentaje = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    masaosea_kg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    masaoseaporcentaje = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    totalcomposicion = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    triceps = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    subescapular = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    suprailiaco = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    abdominal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    totalpliegues = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    brazorelajado = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    brazotensionado = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    muneca = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pecho = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cintura = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    abdomen = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    gluteos = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    muslo = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pantorrilla = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pesograso = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pesomagro = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datosantropometricos'


class Deporte(models.Model):
    iddeporte = models.AutoField(primary_key=True)
    tipodeporte = models.CharField(max_length=800, blank=True, null=True)
    diassemana = models.IntegerField(blank=True, null=True)
    diasdescanso = models.IntegerField(blank=True, null=True)
    duracion = models.IntegerField(blank=True, null=True)
    horario = models.CharField(max_length=800, blank=True, null=True)
    meriendapre = models.CharField(max_length=800, blank=True, null=True)
    meriendapost = models.CharField(max_length=800, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deporte'


class Distribuicionmacronutrientes(models.Model):
    iddistribucionmacro = models.AutoField(primary_key=True)
    proteinas_kg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    proteinas_gramos = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    proteinas_kcal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    proteinas_porcentaje = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    grasas_kg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    grasas_gramos = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    grasas_kcal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    grasas_porcentaje = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    carbohidratos_kg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    carbohidratos_gramos = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    carbohidratos_kcal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    carbohidratos_porcentaje = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_gramos = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_kcal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_porcentaje = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    meriendapremacro = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    meriendapreprote = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    meriendapregrasas = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    meriendaprecarbos = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    meriendaprekcal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    meriendaposmacro = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    meriendaposprote = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    meriendaposgrasas = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    meriendaposcarbos = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    meriendaposkcal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    desayunomacro = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    desayunoposprote = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    desayunoposgrasas = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    desayunoposcarbos = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    desayunoposkcal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    meriendadmacro = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    meriendadprote = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    meriendadgrasas = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    meriendadcarbos = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    meriendadkcal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    almuerzomacro = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    almuerzoprote = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    almuerzograsas = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    almuerzocarbos = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    almuerzokcal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    meriendaamacro = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    meriendaaprote = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    meriendaagrasas = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    meriendaacarbos = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    meriendaakcal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cenamacro = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cenaprote = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cenagrasas = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cenacarbos = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cenakcal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    meriendacmacro = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    meriendacprote = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    meriendacgrasas = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    meriendaccarbos = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    meriendackcal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    totalcomidas_macros = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    totalcomidas_proteinas = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    totalcomidas_grasas = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    totalcomidas_carbos = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    totalcomidas_kcal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    porcadecuacion_proteinas = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    porcadecuacion_grasas = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    porcadecuacion_carbos = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    porcadecuacion_kcal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'distribuicionmacronutrientes'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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


class Estrategianutricional(models.Model):
    idestrategian = models.AutoField(primary_key=True)
    deficit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vet = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    kcaltotal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estrategianutricional'


class Expediente(models.Model):
    idexpediente = models.AutoField(primary_key=True)
    idusuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='idusuario')
    idobservacion = models.ForeignKey('Observacion', models.DO_NOTHING, db_column='idobservacion')
    idindicadorb = models.ForeignKey('Indicadorbioquimico', models.DO_NOTHING, db_column='idindicadorb')
    idhistoriaclinica = models.ForeignKey('Historiaclinica', models.DO_NOTHING, db_column='idhistoriaclinica')
    idginecologico = models.ForeignKey(Aspectosginecologicos, models.DO_NOTHING, db_column='idginecologico')
    idperiodom = models.ForeignKey('Periodomenstrual', models.DO_NOTHING, db_column='idperiodom')
    idpreferenciaa = models.ForeignKey('Preferenciasalimentarias', models.DO_NOTHING, db_column='idpreferenciaa')
    idmedicamento = models.ForeignKey('Medicamento', models.DO_NOTHING, db_column='idmedicamento')
    idconsumo = models.ForeignKey(Consumopreparacionesmedicas, models.DO_NOTHING, db_column='idconsumo')
    idhabitosocial = models.ForeignKey('Habitossociales', models.DO_NOTHING, db_column='idhabitosocial')
    idmetodocomidas = models.ForeignKey('Metodocomidas', models.DO_NOTHING, db_column='idmetodocomidas')
    idtipograsas = models.ForeignKey('Tipograsas', models.DO_NOTHING, db_column='idtipograsas')
    idconsumocomida = models.ForeignKey('Frecuenciaconsumo', models.DO_NOTHING, db_column='idconsumocomida')
    idactividadfisica = models.ForeignKey(Actividadfisica, models.DO_NOTHING, db_column='idactividadfisica')
    iddeporte = models.ForeignKey(Deporte, models.DO_NOTHING, db_column='iddeporte')
    idsuplemento = models.ForeignKey('Suplemento', models.DO_NOTHING, db_column='idsuplemento')
    idcalculon = models.ForeignKey(Calculonutrientes, models.DO_NOTHING, db_column='idcalculon')
    idcomidas = models.ForeignKey(Comidasrealizadas, models.DO_NOTHING, db_column='idcomidas')
    idsignosfisicos = models.ForeignKey('Signosfisicos', models.DO_NOTHING, db_column='idsignosfisicos')
    iddistribucionmacro = models.ForeignKey(Distribuicionmacronutrientes, models.DO_NOTHING, db_column='iddistribucionmacro')
    fechaingreso = models.DateField()
    idplan = models.ForeignKey('Plan', models.DO_NOTHING, db_column='idplan')
    horassueno = models.IntegerField(blank=True, null=True)
    comidafinsemana = models.CharField(max_length=1, blank=True, null=True)
    comidafinsemanadesc = models.CharField(max_length=800, blank=True, null=True)
    idvaloracion = models.ForeignKey('Valoracionantropometrica', models.DO_NOTHING, db_column='idvaloracion')

    class Meta:
        managed = False
        db_table = 'expediente'


class Frecuenciaconsumo(models.Model):
    idconsumocomida = models.AutoField(primary_key=True)
    lechepinitofrecuenia = models.CharField(max_length=1, blank=True, null=True)
    lecheevaporadafrecuenia = models.CharField(max_length=1, blank=True, null=True)
    lechecondensadafrecuenia = models.CharField(max_length=1, blank=True, null=True)
    yogurtfrecuencia = models.CharField(max_length=1, blank=True, null=True)
    manzanafrecuencia = models.CharField(max_length=1, blank=True, null=True)
    bananofrecuencia = models.CharField(max_length=1, blank=True, null=True)
    papayafrecuencia = models.CharField(max_length=1, blank=True, null=True)
    sandiafrecuencia = models.CharField(max_length=1, blank=True, null=True)
    pinafrecuencia = models.CharField(max_length=1, blank=True, null=True)
    mandarinafrecuencia = models.CharField(max_length=1, blank=True, null=True)
    brocolifrecuencia = models.CharField(max_length=1, blank=True, null=True)
    chayotefrecuencia = models.CharField(max_length=1, blank=True, null=True)
    zanahoriafrecuencia = models.CharField(max_length=1, blank=True, null=True)
    pepinofrecuencia = models.CharField(max_length=1, blank=True, null=True)
    lechugafrecuencia = models.CharField(max_length=1, blank=True, null=True)
    repollofrecuencia = models.CharField(max_length=1, blank=True, null=True)
    tomatefrecuencia = models.CharField(max_length=1, blank=True, null=True)
    yucafrecuencia = models.CharField(max_length=1, blank=True, null=True)
    papafrecuencia = models.CharField(max_length=1, blank=True, null=True)
    arrozfrecuencia = models.CharField(max_length=1, blank=True, null=True)
    frijolesfrecuencia = models.CharField(max_length=1, blank=True, null=True)
    lentejasfrecuencia = models.CharField(max_length=1, blank=True, null=True)
    garbanzosfrecuencia = models.CharField(max_length=1, blank=True, null=True)
    pancuadradofrecuencia = models.CharField(max_length=1, blank=True, null=True)
    panbaguettefrecuencia = models.CharField(max_length=1, blank=True, null=True)
    pastasfrecuencia = models.CharField(max_length=1, blank=True, null=True)
    avenafrecuencia = models.CharField(max_length=1, blank=True, null=True)
    tortillafrecuencia = models.CharField(max_length=1, blank=True, null=True)
    galletasfrecuencia = models.CharField(max_length=1, blank=True, null=True)
    cerealesfrecuencia = models.CharField(max_length=1, blank=True, null=True)
    huevofrecuencia = models.CharField(max_length=1, blank=True, null=True)
    embutidofrecuencia = models.CharField(max_length=1, blank=True, null=True)
    jamonfrecuencia = models.CharField(max_length=1, blank=True, null=True)
    atunfrecuencia = models.CharField(max_length=1, blank=True, null=True)
    pollofrecuencia = models.CharField(max_length=1, blank=True, null=True)
    carnemolidafrecuencia = models.CharField(max_length=1, blank=True, null=True)
    chuletafrecuencia = models.CharField(max_length=1, blank=True, null=True)
    bistecfrecuencia = models.CharField(max_length=1, blank=True, null=True)
    salmonfrecuencia = models.CharField(max_length=1, blank=True, null=True)
    mariscosfrecuencia = models.CharField(max_length=1, blank=True, null=True)
    aceitefrecuencia = models.CharField(max_length=1, blank=True, null=True)
    mantequillafrecuencia = models.CharField(max_length=1, blank=True, null=True)
    margarinafrecuencia = models.CharField(max_length=1, blank=True, null=True)
    natillafrecuencia = models.CharField(max_length=1, blank=True, null=True)
    quesocremafrecuencia = models.CharField(max_length=1, blank=True, null=True)
    azucarmesafrecuencia = models.CharField(max_length=1, blank=True, null=True)
    jaleafrecuencia = models.CharField(max_length=1, blank=True, null=True)
    gaseosasfrecuencia = models.CharField(max_length=1, blank=True, null=True)
    dulcesfrecuencia = models.CharField(max_length=1, blank=True, null=True)
    reposteriafrecuencia = models.CharField(max_length=1, blank=True, null=True)
    comidachatarrafrecuencia = models.CharField(max_length=1, blank=True, null=True)
    lechefrecuencia = models.CharField(max_length=1, blank=True, null=True)
    jugosnaturalesfrecuencia = models.CharField(max_length=1, blank=True, null=True)
    jugosazucaradosfrecuencia = models.CharField(max_length=1, blank=True, null=True)
    bebidasenergizantesfrecuencia = models.CharField(max_length=1, blank=True, null=True)
    bevidasdeportivasfrecuencia = models.CharField(max_length=1, blank=True, null=True)
    cafefrecuencia = models.CharField(max_length=1, blank=True, null=True)
    aguafrecuencia = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'frecuenciaconsumo'


class Gastocalorico(models.Model):
    idgasto = models.AutoField(primary_key=True)
    diasentrenamiento = models.IntegerField(blank=True, null=True)
    gastocaldentrenamiento = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    diasdescanso = models.IntegerField(blank=True, null=True)
    gastocalddescanso = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    promediocalorias = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    gastocaldpcalorias = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    minutosaf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ge = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    minutossemana = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    dias = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    gastosemanal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gastocalorico'


class Habitossociales(models.Model):
    idhabitosocial = models.AutoField(primary_key=True)
    consumoalcohol = models.CharField(max_length=1, blank=True, null=True)
    frecuenciaalcohol = models.CharField(max_length=800, blank=True, null=True)
    tipoalcohol = models.CharField(max_length=800, blank=True, null=True)
    cantidadalcohol = models.CharField(max_length=800, blank=True, null=True)
    consumotabaco = models.CharField(max_length=1, blank=True, null=True)
    frecuenciatabaco = models.CharField(max_length=800, blank=True, null=True)
    tipotabaco = models.CharField(max_length=800, blank=True, null=True)
    cantidadtabaco = models.CharField(max_length=800, blank=True, null=True)
    consumodrogas = models.CharField(max_length=1, blank=True, null=True)
    frecuenciadrogas = models.CharField(max_length=800, blank=True, null=True)
    tipodrogas = models.CharField(max_length=800, blank=True, null=True)
    cantidaddrogas = models.CharField(max_length=800, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'habitossociales'


class Historiaclinica(models.Model):
    idhistoriaclinica = models.AutoField(primary_key=True)
    fecha = models.DateField()
    dislipidemiasp = models.CharField(max_length=1, blank=True, null=True)
    dislipidemiasf = models.CharField(max_length=1, blank=True, null=True)
    hipertensionp = models.CharField(max_length=1, blank=True, null=True)
    hipertensionf = models.CharField(max_length=1, blank=True, null=True)
    diabetesp = models.CharField(max_length=1, blank=True, null=True)
    diabetesf = models.CharField(max_length=1, blank=True, null=True)
    ecvp = models.CharField(max_length=1, blank=True, null=True)
    ecvf = models.CharField(max_length=1, blank=True, null=True)
    tiroidesp = models.CharField(max_length=1, blank=True, null=True)
    tiroidesf = models.CharField(max_length=1, blank=True, null=True)
    cancerp = models.CharField(max_length=1, blank=True, null=True)
    cancerf = models.CharField(max_length=1, blank=True, null=True)
    estrenimientop = models.CharField(max_length=1, blank=True, null=True)
    estrenimientof = models.CharField(max_length=1, blank=True, null=True)
    diarreap = models.CharField(max_length=1, blank=True, null=True)
    diarreaf = models.CharField(max_length=1, blank=True, null=True)
    vomitop = models.CharField(max_length=1, blank=True, null=True)
    ssip = models.CharField(max_length=1, blank=True, null=True)
    ssif = models.CharField(max_length=1, blank=True, null=True)
    problemapesop = models.CharField(max_length=1, blank=True, null=True)
    problemapesof = models.CharField(max_length=1, blank=True, null=True)
    ansiedaddepresionp = models.CharField(max_length=1, blank=True, null=True)
    ansiedaddepresionf = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historiaclinica'


class Indicadorbioquimico(models.Model):
    idindicadorb = models.AutoField(primary_key=True)
    fecha = models.DateField()
    colesterol = models.CharField(max_length=800, blank=True, null=True)
    trigliceridos = models.CharField(max_length=800, blank=True, null=True)
    hdl = models.CharField(max_length=800, blank=True, null=True)
    ldl = models.CharField(max_length=800, blank=True, null=True)
    glucosaayunas = models.CharField(max_length=800, blank=True, null=True)
    hemoglobina = models.CharField(max_length=800, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'indicadorbioquimico'


class Medicamento(models.Model):
    idmedicamento = models.AutoField(primary_key=True)
    motivo = models.CharField(max_length=800, blank=True, null=True)
    consumo = models.CharField(max_length=800, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medicamento'


class Metodocomidas(models.Model):
    idmetodocomidas = models.AutoField(primary_key=True)
    frito = models.CharField(max_length=1, blank=True, null=True)
    hervido = models.CharField(max_length=1, blank=True, null=True)
    plancha = models.CharField(max_length=1, blank=True, null=True)
    vapor = models.CharField(max_length=1, blank=True, null=True)
    horno = models.CharField(max_length=1, blank=True, null=True)
    parrilla = models.CharField(max_length=1, blank=True, null=True)
    freidoraaire = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'metodocomidas'


class Observacion(models.Model):
    idobservacion = models.AutoField(primary_key=True)
    fechaobservacion = models.DateField()
    observacion = models.CharField(max_length=800)

    class Meta:
        managed = False
        db_table = 'observacion'


class Ocupacion(models.Model):
    idocupacion = models.AutoField(primary_key=True)
    idusuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='idusuario')
    tipoindustria = models.CharField(max_length=800, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ocupacion'


class Periodomenstrual(models.Model):
    idperiodom = models.AutoField(primary_key=True)
    diasmenstruacion = models.CharField(max_length=800, blank=True, null=True)
    fechaultimamenstruacion = models.DateField(blank=True, null=True)
    sintomasantes = models.CharField(max_length=800, blank=True, null=True)
    sintomasdespues = models.CharField(max_length=800, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'periodomenstrual'


class Plan(models.Model):
    idplan = models.AutoField(primary_key=True)
    idusuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='idusuario')
    inicio = models.DateField()
    fin = models.DateField()
    meta = models.CharField(max_length=800)

    class Meta:
        managed = False
        db_table = 'plan'


class Planalimento(models.Model):
    idplanalimento = models.AutoField(primary_key=True)
    idalimento = models.ForeignKey(Alimento, models.DO_NOTHING, db_column='idalimento')
    porclacteos = models.IntegerField(blank=True, null=True)
    porcvegetales = models.IntegerField(blank=True, null=True)
    porcfrutas = models.IntegerField(blank=True, null=True)
    porcazucar = models.IntegerField(blank=True, null=True)
    porcharinas = models.IntegerField(blank=True, null=True)
    porccarnesbajasgrasa = models.IntegerField(blank=True, null=True)
    porccarnesmoderadasgrasa = models.IntegerField(blank=True, null=True)
    porcgrasas = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'planalimento'


class Plannutricional(models.Model):
    idnutricional = models.AutoField(primary_key=True)
    idplan = models.ForeignKey(Plan, models.DO_NOTHING, db_column='idplan')
    idplanalimento = models.ForeignKey(Planalimento, models.DO_NOTHING, db_column='idplanalimento')
    iddatos = models.ForeignKey(Datosantropometricos, models.DO_NOTHING, db_column='iddatos')

    class Meta:
        managed = False
        db_table = 'plannutricional'


class Preferenciasalimentarias(models.Model):
    idpreferenciaa = models.AutoField(primary_key=True)
    alegiaalimentaria = models.CharField(max_length=1, blank=True, null=True)
    alergiaalimentariadesc = models.CharField(max_length=800, blank=True, null=True)
    intoleranciaalimentaria = models.CharField(max_length=1, blank=True, null=True)
    intoleranciaalimentariadesc = models.CharField(max_length=800, blank=True, null=True)
    lugarcomida = models.CharField(max_length=800, blank=True, null=True)
    cocinaalimento = models.CharField(max_length=1, blank=True, null=True)
    compraalimento = models.CharField(max_length=1, blank=True, null=True)
    calificacionalimentacion = models.IntegerField(blank=True, null=True)
    calificacionapetito = models.IntegerField(blank=True, null=True)
    ansiedadcomida = models.CharField(max_length=1, blank=True, null=True)
    consumoansiedad = models.CharField(max_length=800, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'preferenciasalimentarias'


class Recetas(models.Model):
    idreceta = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=800)
    ingredientes = models.CharField(max_length=800)
    instrucciones = models.CharField(max_length=800)
    notas = models.CharField(max_length=800, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recetas'


class Roles(models.Model):
    idrol = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class Signosfisicos(models.Model):
    idsignosfisicos = models.AutoField(primary_key=True)
    aspectogeneral = models.CharField(max_length=800, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'signosfisicos'


class Suplemento(models.Model):
    idsuplemento = models.AutoField(primary_key=True)
    nombresuplemento = models.CharField(max_length=800, blank=True, null=True)
    marca = models.CharField(max_length=800, blank=True, null=True)
    vecesdia = models.IntegerField(blank=True, null=True)
    diassemana = models.IntegerField(blank=True, null=True)
    dosis = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'suplemento'


class Tasametabolicabasal(models.Model):
    idtmb = models.AutoField(primary_key=True)
    harrisb_tmb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    harrisb_get = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mifflin_tmb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mifflin_get = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    muller_tmb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    muller_get = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cunningham_tmb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cunningham_get = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mcaerdle_tmb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    mcaerdle_get = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    iom_tmb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tasametabolicabasal'


class Tipoactividad(models.Model):
    idtipoactividad = models.AutoField(primary_key=True)
    reposofa = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    muyligerafa = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ligerafa = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    moderadofa = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    severofa = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    festresfa = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    factividadfa = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ftermicofa = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    suma = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipoactividad'


class Tipograsas(models.Model):
    idtipograsas = models.AutoField(primary_key=True)
    aceite = models.CharField(max_length=1, blank=True, null=True)
    mantequilla = models.CharField(max_length=1, blank=True, null=True)
    margarina = models.CharField(max_length=1, blank=True, null=True)
    spray = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipograsas'


class Usuarios(models.Model):
    idusuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=800)
    primerapellido = models.CharField(max_length=800)
    segundoapellido = models.CharField(max_length=800, blank=True, null=True)
    usuario = models.CharField(max_length=800)
    clave = models.CharField(max_length=800)
    email = models.CharField(max_length=800, blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)
    identificacion = models.CharField(max_length=800, blank=True, null=True)
    fechanacimiento = models.DateField(blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    idrol = models.ForeignKey(Roles, models.DO_NOTHING, db_column='idrol')
    estado = models.CharField(max_length=800, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios'


class Valoracionantropometrica(models.Model):
    idvaloracion = models.AutoField(primary_key=True)
    iddatos = models.ForeignKey(Datosantropometricos, models.DO_NOTHING, db_column='iddatos')
    idgasto = models.ForeignKey(Gastocalorico, models.DO_NOTHING, db_column='idgasto')
    idtipoactividad = models.ForeignKey(Tipoactividad, models.DO_NOTHING, db_column='idtipoactividad')
    idtmb = models.ForeignKey(Tasametabolicabasal, models.DO_NOTHING, db_column='idtmb')
    idestrategian = models.ForeignKey(Estrategianutricional, models.DO_NOTHING, db_column='idestrategian')
    nombre = models.CharField(max_length=800, blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    pesokg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tallamts = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    edadanho = models.IntegerField(blank=True, null=True)
    pm = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cm = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ca = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cca = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    masagrasafaulkner_kg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    masagrasafaulkner_porc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    masmuscularlee_kg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    masmuscularlee_porc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    masresidualwurch_kg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    masresidualwurch_porc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    masoseadiferencia_kg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    masoseadiferencia_porc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    totalmasa_kg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    totalmasa_porc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    actwatson_litros = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    actwatson_porc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    acthume_litros = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    acthume_porc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    calculoagua_litros = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    calculoagua_porc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    imc_valor = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    imc_diagnostico = models.CharField(max_length=800, blank=True, null=True)
    circabdominal_valor = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    circabdominal_diagnostico = models.CharField(max_length=800, blank=True, null=True)
    rcinturacadera_valor = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    rcinturacadera_diagnostico = models.CharField(max_length=800, blank=True, null=True)
    composicioncorporal_valor = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pesoideal_pequena = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pesoideal_mediana = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pesoideal_grande = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pesoideal_ada = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pesoajustado = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    diferenciapeso_kg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pesometa_kg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'valoracionantropometrica'
