# Generated by Django 5.1.2 on 2024-10-18 00:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_usuarios_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Generos',
            fields=[
                ('generos_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_genero', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'generos',
            },
        ),
        migrations.AddField(
            model_name='usuarios',
            name='fk_generos',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.generos'),
            preserve_default=False,
        ),
    ]
