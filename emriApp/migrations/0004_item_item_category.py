# Generated by Django 5.1.3 on 2024-11-26 17:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emriApp', '0003_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='emriApp.category'),
        ),
    ]