# Generated by Django 4.0.2 on 2022-02-06 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('despesa', '0002_despesa_data_despesa_parcelas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='despesa',
            old_name='data',
            new_name='data_da_despesa',
        ),
        migrations.AlterField(
            model_name='despesa',
            name='descricao',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]
