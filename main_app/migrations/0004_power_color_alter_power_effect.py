# Generated by Django 5.0.6 on 2024-05-13 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_power_alter_feeding_options_alter_feeding_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='power',
            name='color',
            field=models.CharField(default='white', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='power',
            name='effect',
            field=models.CharField(max_length=100),
        ),
    ]
