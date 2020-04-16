# Generated by Django 3.0 on 2020-04-16 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminLoginModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('otp', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StateModel',
            fields=[
                ('stateno', models.AutoField(primary_key=True, serialize=False)),
                ('statename', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CityModel',
            fields=[
                ('cityno', models.AutoField(primary_key=True, serialize=False)),
                ('cityname', models.CharField(max_length=30, unique=True)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='akr_admin.StateModel')),
            ],
        ),
        migrations.CreateModel(
            name='AreaModel',
            fields=[
                ('area_no', models.AutoField(primary_key=True, serialize=False)),
                ('area_name', models.CharField(max_length=50)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='akr_admin.CityModel')),
            ],
        ),
    ]