# Generated by Django 3.2.12 on 2022-05-26 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_review_rank'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='video',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='vote_count',
        ),
    ]
