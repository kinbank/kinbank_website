# Generated by Django 3.0.5 on 2021-07-28 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kb', '0005_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='full name')),
            ],
        ),
    ]