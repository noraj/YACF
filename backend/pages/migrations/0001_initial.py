# Generated by Django 2.1.8 on 2019-10-02 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=15, unique=True)),
                ('name', models.CharField(max_length=15)),
                ('content', models.CharField(max_length=5000)),
                ('authenticated', models.BooleanField(default=True)),
            ],
        ),
    ]
