# Generated by Django 5.1.6 on 2025-02-24 08:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QAMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct_choice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.choice')),
                ('question', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.question')),
            ],
        ),
    ]
