# Generated by Django 5.0.1 on 2024-02-13 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='imagefilter',
            field=models.CharField(choices=[('Nature', 'Nature'), ('Architect', 'Architect'), ('Preprimary', 'Preprimary')], default='option1', max_length=20),
        ),
    ]
