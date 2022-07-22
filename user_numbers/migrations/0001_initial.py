# Generated by Django 4.0.6 on 2022-07-21 20:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserNumbersModel',
            fields=[
                ('id', models.AutoField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('numbers', models.CharField(max_length=100)),
                ('favorite', models.BooleanField(default=False)),
            ],
        ),
    ]
