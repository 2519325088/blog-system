# Generated by Django 2.1.7 on 2019-04-25 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aname', models.CharField(max_length=90)),
                ('acontent', models.TextField()),
                ('atime', models.DateTimeField(auto_now_add=True)),
                ('axtime', models.DateTimeField(auto_now_add=True)),
                ('apageview', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crname', models.CharField(max_length=20)),
                ('cemail', models.EmailField(blank=True, max_length=254)),
                ('chttp', models.CharField(max_length=30)),
                ('cname', models.TextField()),
                ('ctime', models.DateTimeField(auto_now_add=True)),
                ('carticle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogstystem.Article')),
            ],
        ),
        migrations.CreateModel(
            name='Fei',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Ladel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lname', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=21)),
                ('upasswd', models.CharField(max_length=21)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='alei',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogstystem.Fei'),
        ),
        migrations.AddField(
            model_name='article',
            name='auser_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogstystem.Users'),
        ),
        migrations.AddField(
            model_name='article',
            name='larticle_id',
            field=models.ManyToManyField(to='blogstystem.Ladel'),
        ),
    ]
