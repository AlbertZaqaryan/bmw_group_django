# Generated by Django 4.1.7 on 2023-03-21 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_subtitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Home name')),
            ],
        ),
    ]
