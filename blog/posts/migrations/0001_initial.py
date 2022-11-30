# Generated by Django 4.1.3 on 2022-11-30 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('b_users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('blog_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='b_users.buser')),
            ],
            options={
                'db_table': 'blog_posts',
            },
        ),
    ]
