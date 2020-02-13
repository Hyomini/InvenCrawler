# Generated by Django 2.2.5 on 2020-02-13 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('link', models.URLField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname_text', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['nickname_text'],
            },
        ),
        migrations.CreateModel(
            name='Cmt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date', models.CharField(max_length=20)),
                ('link', models.URLField()),
                ('nickname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parsed_data.Member')),
            ],
        ),
    ]
