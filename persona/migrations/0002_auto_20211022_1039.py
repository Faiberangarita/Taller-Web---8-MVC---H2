# Generated by Django 3.2.8 on 2021-10-22 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='email',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='password',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='residencia',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='telefono',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='tipodocumento',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='usuario',
        ),
    ]