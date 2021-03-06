# Generated by Django 3.0.1 on 2020-01-03 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edition',
            name='game_type',
            field=models.CharField(choices=[('B', 'Base Game'), ('E', 'Expansion'), ('M', 'Expansion Combination')], default='B', max_length=1, verbose_name='edition type'),
        ),
        migrations.AlterField(
            model_name='edition',
            name='max_players',
            field=models.CharField(choices=[('24', '2-4'), ('34', '3-4'), ('56', '5-6')], default='34', max_length=3, verbose_name='max player count'),
        ),
        migrations.AlterField(
            model_name='edition',
            name='name',
            field=models.CharField(max_length=75, verbose_name="edition's nickname"),
        ),
    ]
