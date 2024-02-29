# Generated by Django 5.0.2 on 2024-02-29 05:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_id', models.CharField(max_length=100)),
                ('user_contact', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Delivered',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField()),
                ('comment', models.CharField(max_length=100)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.card')),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryException',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField()),
                ('comment', models.CharField(max_length=100)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.card')),
            ],
        ),
        migrations.CreateModel(
            name='Pickup',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField()),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.card')),
            ],
        ),
        migrations.CreateModel(
            name='Returned',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField()),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.card')),
            ],
        ),
        migrations.DeleteModel(
            name='CardStatus',
        ),
    ]
