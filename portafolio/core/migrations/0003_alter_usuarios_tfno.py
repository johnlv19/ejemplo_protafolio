# Generated by Django 4.1.5 on 2023-02-01 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_usuarios_tfno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='tfno',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]