# Generated by Django 3.0.2 on 2020-01-26 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('imageUrl', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('available', models.BooleanField()),
                ('color', models.CharField(choices=[('1', 'Green'), ('2', 'Yellow'), ('3', 'Blue'), ('4', 'Black'), ('5', 'White')], default='Green', max_length=20)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.Author')),
            ],
        ),
        migrations.DeleteModel(
            name='Hotel',
        ),
    ]
