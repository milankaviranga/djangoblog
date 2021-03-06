# Generated by Django 3.0.7 on 2020-08-20 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=264, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('title', models.CharField(max_length=264, unique=True)),
                ('img_name', models.CharField(max_length=100, unique=True)),
                ('text', models.CharField(max_length=3500, unique=True)),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Catagory')),
            ],
        ),
    ]
