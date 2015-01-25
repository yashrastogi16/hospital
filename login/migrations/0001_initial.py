# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='disease',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('disease_symptom', models.CharField(max_length=50)),
                ('prescription', models.CharField(max_length=50)),
                ('reports_attacments', models.CharField(max_length=50)),
                ('detected_disease', models.CharField(max_length=50)),
                ('cured', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('doctorname', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(null=True, upload_to=b'projectimg/', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=100, verbose_name=b'First Name')),
                ('lastname', models.CharField(max_length=100, verbose_name=b'Last Name')),
                ('age', models.CharField(max_length=5, verbose_name=b'Age')),
                ('mobile', models.CharField(max_length=15, verbose_name=b'Mobile')),
                ('city', models.CharField(max_length=60, verbose_name=b'City')),
                ('date', models.DateField(verbose_name=b'Date')),
                ('email', models.EmailField(max_length=254)),
                ('createdat', models.DateTimeField(auto_now_add=True)),
                ('doctor', models.ForeignKey(to='login.doctor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='image',
            name='patient',
            field=models.ForeignKey(to='login.patient'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='disease',
            name='patient',
            field=models.ForeignKey(to='login.patient'),
            preserve_default=True,
        ),
    ]
