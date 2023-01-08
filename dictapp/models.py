from django.db import models

#from django.conf import settings

class dictclass(models.Model):
    id =            models.AutoField(primary_key=True)
    palavra =       models.TextField(max_length=255, blank=True, default='')
    palavratrad =   models.TextField(max_length=1000, blank=True, default='')
    frase =         models.TextField(max_length=1000, blank=True, default='')
    frasetrad =     models.TextField(max_length=1000, blank=True, default='')
    frase2 =        models.TextField(max_length=1000, blank=True, default='')
    frasetrad2 =    models.TextField(max_length=1000, blank=True, default='')
    frase3 =        models.TextField(max_length=1000, blank=True, default='')
    frasetrad3 =    models.TextField(max_length=1000, blank=True, default='')
    frase4 =        models.TextField(max_length=1000, blank=True, default='')
    frasetrad4 =    models.TextField(max_length=1000, blank=True, default='')
    frase5 =        models.TextField(max_length=1000, blank=True, default='')
    frasetrad5 =    models.TextField(max_length=1000, blank=True, default='')
    figura1 =       models.TextField(max_length=1000, null=False, blank=False)
    som1 =          models.CharField(max_length=1000, null=False, blank=False)
    Ordem = models.CharField(max_length=3, blank=True, default='')
    suaresposta1 =   models.TextField(max_length=1000, blank=True, default='')
    suaresposta2 =   models.TextField(max_length=1000, blank=True, default='')
    suaresposta3 =   models.TextField(max_length=1000, blank=True, default='')
    title =         models.CharField(max_length=200, blank=True, default='')
    image =         models.ImageField(upload_to='images')
    qualtabela2 =   models.CharField(max_length=255, blank=True, default='')
    ondetabela =    models.CharField(max_length=300, blank=True, default='')
    Acertou		 =       models.CharField(max_length=3, blank=True, default='')
    Jafoi		 =       models.CharField(max_length=3, blank=True, default='')
    Corretas	 =       models.CharField(max_length=3, blank=True, default='')
    Porcentagem	 =       models.CharField(max_length=3, blank=True, default='')

    #qualtabela =    models.FileField(upload_to='', max_length=254)
    #qualtabela = models.FileField()
    #qualtabela = models.FileField(upload_to=None, blank=True, null=True)
    #qualtabela =    models.FileField(upload_to=None, max_length=254)


    # https://www.geeksforgeeks.org/filefield-django-models/
    # field_name = models.FileField(upload_to=None, max_length=254, **options)


    def __str__(self):
        return self.palavra + ' ' + self.frase

    objects = models.Manager()
    objetos = models.Manager()


