 path('persona/new', views.new_persona, name='create_persona'),



 nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    tipodocumento = models.IntegerField(max_length=1)
    documento = models.IntegerField(max_length=15)
    residencia = models.CharField(max_length=100)
    fechanacimiento = models.DateField
    email = models.CharField(max_length=50)
    telefono = models.IntegerField(max_length=15)
    usuario = models.CharField(max_length=30)
    password = models.CharField(max_length=30)