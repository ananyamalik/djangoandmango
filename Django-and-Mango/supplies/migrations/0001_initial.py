# Generated by Django 2.0.9 on 2019-02-06 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=350)),
                ('quantity', models.IntegerField()),
                ('rate', models.IntegerField()),
                ('requirements', models.IntegerField()),
                ('order', models.BooleanField(default=False)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=350)),
                ('contact', models.CharField(max_length=10)),
                ('area', models.TextField()),
                ('available', models.BooleanField(default=False)),
                ('slug', models.SlugField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplies.Item')),
            ],
        ),
    ]
