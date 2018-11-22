# Generated by Django 2.0.9 on 2018-11-22 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Depoimentos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='depoimentos/imagens', verbose_name='Imagem')),
                ('descrição', models.TextField(blank=True, null=True, verbose_name='Descricao')),
                ('autor', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Depoimentos',
                'verbose_name': 'Depoimentos',
            },
        ),
        migrations.CreateModel(
            name='Inicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField(blank=True, max_length=100, null=True, verbose_name='Titulo')),
                ('imagem', models.ImageField(upload_to='quemsomos/imagens', verbose_name='Imagem')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descricao')),
            ],
            options={
                'verbose_name_plural': 'Inicio',
                'verbose_name': 'Inicio',
            },
        ),
        migrations.CreateModel(
            name='Parceiros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='parceiros/imagens', verbose_name='Imagem')),
            ],
            options={
                'verbose_name_plural': 'Parceiros',
                'verbose_name': 'Parceiros',
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='portfolio/imagens', verbose_name='Imagem')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descricao')),
            ],
            options={
                'verbose_name_plural': 'Portfolio',
                'verbose_name': 'Portfolio',
            },
        ),
        migrations.CreateModel(
            name='Quemsomos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='quemsomos/imagens', verbose_name='Imagem')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descricao')),
            ],
            options={
                'verbose_name_plural': 'Quem somos',
                'verbose_name': 'Quem somos',
            },
        ),
        migrations.CreateModel(
            name='Servicos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField(blank=True, max_length=100, null=True, verbose_name='Titulo')),
                ('imagem', models.ImageField(upload_to='servicos/im = agens', verbose_name='Imagem')),
                ('descricao1', models.TextField(blank=True, null=True, verbose_name='Descricao1')),
                ('descricao2', models.TextField(blank=True, null=True, verbose_name='Descricao2')),
            ],
            options={
                'verbose_name_plural': 'Servicos',
                'verbose_name': 'Servicos',
            },
        ),
    ]