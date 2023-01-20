# Generated by Django 4.1.1 on 2022-11-22 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_rename_producto_reserva_product_alter_orden_estatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='estatus',
            field=models.CharField(choices=[('Completado', 'Completado'), ('En envio', 'En envio'), ('Pendiente', 'Pendiente')], default='Pendiente', max_length=150),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
    ]