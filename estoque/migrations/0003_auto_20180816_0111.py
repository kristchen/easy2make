# Generated by Django 2.1 on 2018-08-16 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0002_auto_20180810_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(upload_to='imagens/'),
        ),
    ]
