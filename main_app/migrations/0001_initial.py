# Generated by Django 4.2.8 on 2023-12-27 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feeding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='feeding date')),
                ('meal', models.CharField(choices=[('B', 'Breakfast'), ('L', 'Lunch'), ('D', 'Dinner')], default='B', max_length=1)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Toy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Finch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species', models.CharField(max_length=100)),
                ('scientific_name', models.CharField(max_length=100)),
                ('average_lifespan', models.IntegerField()),
                ('habitat', models.CharField(max_length=100)),
                ('diet', models.CharField(max_length=100)),
                ('toys', models.ManyToManyField(to='main_app.toy')),
            ],
        ),
    ]
