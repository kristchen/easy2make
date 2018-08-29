# Generated by Django 2.1 on 2018-08-29 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='situacao',
            field=models.CharField(choices=[('P', 'Pendente'), ('F', 'Finalizada')], default='P', max_length=1),
        ),
        migrations.AlterField(
            model_name='itemvenda',
            name='quantidade',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
