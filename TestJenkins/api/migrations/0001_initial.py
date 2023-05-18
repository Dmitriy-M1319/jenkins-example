# Generated by Django 4.2.1 on 2023-05-18 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(max_length=60)),
                ('name', models.CharField(max_length=60)),
                ('engine', models.CharField(max_length=40)),
                ('cylyner_count', models.IntegerField()),
                ('oil_type', models.IntegerField()),
            ],
            options={
                'db_table': 'cars',
            },
        ),
    ]