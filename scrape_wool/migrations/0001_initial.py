# Generated by Django 3.2.5 on 2022-06-26 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WoolItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('price', models.FloatField()),
                ('currency', models.CharField(default='$', max_length=10)),
                ('needle_size', models.FloatField()),
                ('composition', models.CharField(max_length=200)),
            ],
        ),
    ]
