# Generated by Django 3.2.3 on 2021-05-28 16:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MovieName', models.CharField(max_length=255)),
                ('MovieGenre', models.CharField(max_length=100)),
                ('ReleaseDate', models.DateField()),
                ('MovieReviewer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Movies',
            },
        ),
        migrations.CreateModel(
            name='MovieType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MovieTypeName', models.CharField(max_length=255)),
                ('MovieDescription', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'MovieType',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MovieReview', models.TextField()),
                ('ReviewDate', models.DateField()),
                ('Movieid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieR.movies')),
            ],
            options={
                'db_table': 'Reviews',
            },
        ),
    ]
