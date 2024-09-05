# Generated by Django 5.1 on 2024-09-03 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='user_signup',
            fields=[
                ('user_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=120)),
                ('role', models.CharField(max_length=20)),
            ],
        ),
    ]