# Generated by Django 3.2.15 on 2022-10-31 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomedaapp', '0006_rename_descrição_galeria_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='galeria',
            name='data',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='galeria',
            name='img',
            field=models.ImageField(upload_to='C:\\Users\\tfschmitz\\Downloads\\Capuchinhos-main\\projetointegrado\\media'),
        ),
    ]
