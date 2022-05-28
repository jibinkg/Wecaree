# Generated by Django 3.2.9 on 2022-05-28 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bookingform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Age', models.IntegerField()),
                ('Gender', models.CharField(max_length=10)),
                ('Address', models.CharField(max_length=50)),
                ('Place', models.CharField(max_length=25)),
                ('District', models.CharField(max_length=15)),
                ('State', models.CharField(max_length=20)),
                ('ContactNo', models.IntegerField()),
                ('Paymentmethod', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('cls', models.IntegerField()),
            ],
        ),
    ]
