# Generated by Django 4.2.5 on 2023-09-12 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('idAlumnos', models.IntegerField(db_column='idAlumno', primary_key=True, serialize=False)),
                ('nameAlumno', models.CharField(db_column='nameAlumno', max_length=100)),
            ],
            options={
                'db_table': 'Alumnos',
            },
        ),
    ]
