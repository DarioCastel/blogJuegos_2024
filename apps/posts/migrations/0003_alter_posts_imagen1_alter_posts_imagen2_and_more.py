# Generated by Django 5.1.2 on 2024-10-23 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_user_icono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='imagen1',
            field=models.ImageField(default='posts/default.jpg', upload_to='posts'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='imagen2',
            field=models.ImageField(blank=True, null=True, upload_to='posts'),
        ),
        migrations.AlterField(
            model_name='user',
            name='icono',
            field=models.ImageField(blank=True, default='usuarios/default.png', null=True, upload_to='usuarios'),
        ),
    ]