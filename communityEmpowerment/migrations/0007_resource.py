# Generated by Django 5.0.7 on 2025-02-26 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communityEmpowerment', '0006_companymeta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=100, unique=True)),
                ('resource_link', models.URLField()),
            ],
        ),
    ]