# Generated by Django 3.2.15 on 2022-10-20 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomedaapp', '0004_auto_20221015_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='galeria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descrição', models.CharField(max_length=225)),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
    ]
