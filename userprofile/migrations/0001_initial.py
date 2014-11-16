# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('departamento', models.CharField(max_length=40)),
                ('documento', models.PositiveSmallIntegerField(default=5, choices=[(0, b'DNI'), (5, b'PARTIDA'), (10, b'MILITAR'), (15, b'RUC')])),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('fecha', models.DateField()),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['fecha'],
                'permissions': (('list_app', 'Can view list ap'), ('view_app', 'Can view ap'), ('add_app', 'Can add ap'), ('change_app', 'Can change ap'), ('delete_app', 'Can delete ap')),
            },
            bases=(models.Model,),
        ),
    ]
