# Generated by Django 3.0 on 2020-10-14 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CiscoData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sapid', models.CharField(max_length=18)),
                ('hostname', models.CharField(max_length=14)),
                ('loopback', models.CharField(max_length=17)),
                ('macaddress', models.CharField(max_length=17)),
            ],
        ),
    ]
