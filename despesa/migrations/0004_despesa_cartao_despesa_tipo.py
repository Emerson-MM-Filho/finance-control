# Generated by Django 4.0.2 on 2022-02-12 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cartao', '0001_initial'),
        ('despesa', '0003_rename_data_despesa_data_da_despesa_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='despesa',
            name='cartao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='cartao.cartao'),
        ),
        migrations.AddField(
            model_name='despesa',
            name='tipo',
            field=models.CharField(choices=[('Crédito', 'Crédito'), ('Débito', 'Débito')], default=('Crédito', 'Crédito'), max_length=255),
        ),
    ]
