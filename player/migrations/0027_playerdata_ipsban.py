# Generated by Django 2.2.7 on 2019-11-05 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0026_auto_20191103_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='playerdata',
            name='ipsBan',
            field=models.TextField(default='[]'),
        ),
    ]
