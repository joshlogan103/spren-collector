# Generated by Django 5.0.6 on 2024-05-14 17:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_spren_powers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Radiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('origin', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Interaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('date', models.DateField(verbose_name='Interaction date')),
                ('spren', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.spren')),
                ('radiants', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.radiant')),
            ],
        ),
        migrations.AddField(
            model_name='spren',
            name='radiants',
            field=models.ManyToManyField(through='main_app.Interaction', to='main_app.radiant'),
        ),
    ]
