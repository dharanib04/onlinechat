# Generated by Django 4.2.5 on 2024-01-05 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatroom', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user1', models.CharField(max_length=20)),
                ('user2', models.CharField(max_length=20)),
                ('status', models.CharField(default='pending', max_length=20)),
            ],
        ),
    ]