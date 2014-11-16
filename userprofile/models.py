from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    PRIORITY_LIST = (
        (0, 'DNI'),
        (5, 'PARTIDA'),
        (10, 'MILITAR'),
        (15, 'RUC'),
    )
    departamento = models.CharField(max_length=40)  #tiltle
    usuario = models.ForeignKey(User) #owner
    documento = models.PositiveSmallIntegerField(choices=PRIORITY_LIST, default=5)#prioryti
    added_on = models.DateTimeField(auto_now_add=True)
    fecha = models.DateField()#due on
    
    class Meta:
        permissions = (
            ('list_app', 'Can view list ap'),
            ('view_app', 'Can view ap'),
            ('add_app', 'Can add ap'),
            ('change_app', 'Can change ap'),
            ('delete_app', 'Can delete ap'),
        )
        ordering = ['fecha']
    def __unicode__(self):
        return u"%s" % self.usuario
    @models.permalink
    def get_absolute_url(self):
        return ('app_detail', [int(self.pk)])



