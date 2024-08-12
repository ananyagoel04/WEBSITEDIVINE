# Generated by Django 4.1.13 on 2024-08-08 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('image_title', models.CharField(max_length=50)),
                ('image', models.ImageField(default=None, null=True, upload_to='homeimg/environment/')),
            ],
        ),
        migrations.CreateModel(
            name='Homeimg',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('image_title', models.CharField(max_length=50)),
                ('image', models.ImageField(default=None, null=True, upload_to='homeimg/home/')),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('image_title', models.CharField(max_length=50)),
                ('image', models.ImageField(default=None, null=True, upload_to='homeimg/programs/')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('stars', models.IntegerField()),
                ('review', models.CharField(max_length=225)),
                ('image_title', models.CharField(max_length=50)),
                ('image', models.ImageField(default=None, null=True, upload_to='homeimg/reviews/')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=100)),
                ('image_title', models.CharField(max_length=50)),
                ('image', models.ImageField(default=None, null=True, upload_to='homeimg/teachers/')),
            ],
        ),
        migrations.CreateModel(
            name='VisionMission',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('image_title', models.CharField(max_length=50)),
                ('image', models.ImageField(default=None, null=True, upload_to='homeimg/vision/')),
            ],
        ),
    ]