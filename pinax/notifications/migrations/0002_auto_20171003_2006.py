# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 20:06
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pinax_notifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticesetting',
            name='scoping_content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contenttypes.ContentType'),
        ),
    ]
