# Generated by Django 4.2.5 on 2023-10-18 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_usuario_last_login_alter_usuario_contrausuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvisosRecomendaciones',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('opcion_avisos', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ConoceNumerosEmergencia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('opcion_cne', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ConoceServiciosEmergencia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('opcion_cse', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MapaInteractivo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('opcion_mapa', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PaletaColores',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('opcion_paleta', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RapidezServicio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('opcion_rapidez', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UsarAppEmergencia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('opcion_usarapp', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Uso911',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('opcion_uso911', models.CharField(max_length=255)),
            ],
        ),
    ]
