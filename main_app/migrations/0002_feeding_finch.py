# Generated by Django 4.2.8 on 2024-01-03 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feeding',
            name='finch',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='main_app.finch'),
            preserve_default=False,
        ),
    ]
