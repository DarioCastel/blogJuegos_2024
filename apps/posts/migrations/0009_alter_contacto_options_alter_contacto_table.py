# Generated by Django 5.1.2 on 2024-10-24 03:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_rename_emai_contacto_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contacto',
            options={'verbose_name': 'Contacto', 'verbose_name_plural': 'Contacto'},
        ),
        migrations.AlterModelTable(
            name='contacto',
            table='Contacto',
        ),
    ]