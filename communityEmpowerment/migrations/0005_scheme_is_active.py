# Generated by Django 5.0.7 on 2025-02-25 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communityEmpowerment', '0004_faq'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheme',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]