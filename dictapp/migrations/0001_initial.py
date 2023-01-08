# Generated by Django 4.1.5 on 2023-01-06 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dictclass',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('palavra', models.TextField(blank=True, default='', max_length=255)),
                ('palavratrad', models.TextField(blank=True, default='', max_length=1000)),
                ('frase', models.TextField(blank=True, default='', max_length=1000)),
                ('frasetrad', models.TextField(blank=True, default='', max_length=1000)),
                ('frase2', models.TextField(blank=True, default='', max_length=1000)),
                ('frasetrad2', models.TextField(blank=True, default='', max_length=1000)),
                ('frase3', models.TextField(blank=True, default='', max_length=1000)),
                ('frasetrad3', models.TextField(blank=True, default='', max_length=1000)),
                ('frase4', models.TextField(blank=True, default='', max_length=1000)),
                ('frasetrad4', models.TextField(blank=True, default='', max_length=1000)),
                ('frase5', models.TextField(blank=True, default='', max_length=1000)),
                ('frasetrad5', models.TextField(blank=True, default='', max_length=1000)),
                ('figura1', models.TextField(max_length=1000)),
                ('som1', models.CharField(max_length=1000)),
                ('Ordem', models.CharField(blank=True, default='', max_length=3)),
                ('suaresposta1', models.TextField(blank=True, default='', max_length=1000)),
                ('suaresposta2', models.TextField(blank=True, default='', max_length=1000)),
                ('suaresposta3', models.TextField(blank=True, default='', max_length=1000)),
                ('title', models.CharField(blank=True, default='', max_length=200)),
                ('image', models.ImageField(upload_to='images')),
                ('qualtabela2', models.CharField(blank=True, default='', max_length=255)),
                ('ondetabela', models.CharField(blank=True, default='', max_length=300)),
                ('Acertou', models.CharField(blank=True, default='', max_length=3)),
                ('Jafoi', models.CharField(blank=True, default='', max_length=3)),
                ('Corretas', models.CharField(blank=True, default='', max_length=3)),
                ('Porcentagem', models.CharField(blank=True, default='', max_length=3)),
            ],
        ),
    ]