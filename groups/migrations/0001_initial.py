# Generated by Django 4.2.2 on 2023-06-06 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scientifc_name', models.CharField(max_length=50, unique=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
