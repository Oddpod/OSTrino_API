# Generated by Django 2.1.4 on 2019-04-20 16:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ostdb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('public', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag', models.SlugField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='ost',
            name='show',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ostdb.Show'),
        ),
        migrations.RemoveField(
            model_name='ost',
            name='tags',
        ),
        migrations.AlterField(
            model_name='ost',
            name='video_id',
            field=models.CharField(max_length=12, unique=True),
        ),
        migrations.AddField(
            model_name='playlist',
            name='osts',
            field=models.ManyToManyField(blank=True, to='ostdb.OST'),
        ),
        migrations.AddField(
            model_name='ost',
            name='tags',
            field=models.ManyToManyField(to='ostdb.Tag'),
        ),
        migrations.AlterUniqueTogether(
            name='playlist',
            unique_together={('created_by', 'name')},
        ),
    ]
