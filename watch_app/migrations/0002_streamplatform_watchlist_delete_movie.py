# Generated by Django 5.1.2 on 2024-10-10 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StreamPlatform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('about', models.CharField(max_length=150)),
                ('url', models.URLField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WatchList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('storyline', models.CharField(max_length=250)),
                ('rating', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
    ]
