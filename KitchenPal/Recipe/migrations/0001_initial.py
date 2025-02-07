# Generated by Django 2.0.3 on 2018-06-17 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('recipe_ID', models.IntegerField(primary_key='True', serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('instructions', models.CharField(max_length=400)),
                ('cooking_time', models.IntegerField()),
                ('servings', models.IntegerField()),
            ],
        ),
    ]
