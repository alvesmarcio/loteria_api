# Generated by Django 4.0.6 on 2022-07-27 17:17

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
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('numbers', models.CharField(max_length=100)),
            ],
        ),
    ]
