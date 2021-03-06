# Generated by Django 3.2.8 on 2022-01-19 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0014_auto_20211029_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='knowledge',
            name='alt',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FileField(blank=True, upload_to='project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='tags',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='service',
            name='alt',
            field=models.CharField(max_length=20),
        ),
    ]
