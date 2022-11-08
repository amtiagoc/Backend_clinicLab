# Generated by Django 4.1.3 on 2022-11-05 17:55

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('notes', django_mysql.models.ListTextField(models.CharField(max_length=500), size=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]