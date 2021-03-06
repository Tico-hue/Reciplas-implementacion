# Generated by Django 3.0 on 2020-11-15 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=45)),
                ('apellido', models.TextField(max_length=45)),
                ('CUIT', models.IntegerField(max_length=8)),
                ('razon_social', models.TextField(max_length=45)),
                ('direccion', models.TextField(max_length=45)),
                ('localidad', models.TextField(max_length=45)),
                ('provincia', models.TextField(max_length=45)),
                ('telefono', models.TextField()),
                ('mail', models.TextField()),
            ],
        ),
    ]
