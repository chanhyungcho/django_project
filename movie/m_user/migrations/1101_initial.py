# Generated by Django 4.1.3 on 2022-11-29 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('image_url', models.TextField()),
                ('address', models.TextField()),
                ('detail_address', models.TextField()),
            ],
            options={
                'db_table': 'Cinema',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('director', models.TextField()),
                ('description', models.TextField()),
                ('poster_url', models.TextField()),
                ('running_time', models.IntegerField()),
                ('age_rating', models.IntegerField()),
            ],
            options={
                'db_table': 'Movie',
            },
        ),
        migrations.CreateModel(
            name='MUser',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('email', models.TextField()),
                ('nickname', models.TextField()),
                ('password', models.TextField()),
                ('age', models.IntegerField()),
            ],
            options={
                'db_table': 'm_user',
            },
        ),
        migrations.CreateModel(
            name='Showtime',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('start_time', models.TextField()),
                ('end_time', models.TextField()),
            ],
            options={
                'db_table': 'Showtime',
            },
        ),
        migrations.CreateModel(
            name='Theater',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('seat', models.TextField()),
            ],
            options={
                'db_table': 'Theater',
            },
        ),
        migrations.CreateModel(
            name='TheaterTicket',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
            ],
            options={
                'db_table': 'TheaterTicket',
            },
        ),
    ]