# Generated by Django 3.2.8 on 2021-10-28 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0007_auto_20211028_1545'),
    ]

    operations = [
        migrations.RenameField(
            model_name='knowledge',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='title',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='knowledge',
            name='alt',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
