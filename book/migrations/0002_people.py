# Generated by Django 3.2.8 on 2021-11-24 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250, unique=True)),
                ('last_name', models.CharField(max_length=250, unique=True)),
                ('birthday', models.DateField(max_length=8)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=10, unique=True)),
                ('house_name', models.CharField(max_length=250, unique=True)),
                ('city', models.CharField(max_length=250, unique=True)),
                ('district', models.CharField(max_length=250, unique=True)),
                ('pincode', models.CharField(max_length=6, unique=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
