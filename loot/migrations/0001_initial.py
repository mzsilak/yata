# Generated by Django 2.0.5 on 2019-10-04 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NPC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tId', models.IntegerField(default=0)),
                ('name', models.CharField(default='?', max_length=20)),
                ('status', models.CharField(default='Ok', max_length=20)),
                ('hospitalTS', models.IntegerField(default=0)),
                ('updateTS', models.IntegerField(default=0)),
            ],
        ),
    ]
