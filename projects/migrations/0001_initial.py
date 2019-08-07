# Generated by Django 2.2.3 on 2019-08-04 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Repo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('display_name', models.CharField(max_length=150)),
                ('readme_html', models.TextField()),
                ('sequence', models.IntegerField(default=100)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
                ('no_update', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('sequence', 'name'),
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('url', models.CharField(max_length=30)),
                ('image_url', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('sequence', models.IntegerField(default=100)),
                ('repos', models.ManyToManyField(to='projects.Repo')),
            ],
            options={
                'ordering': ('sequence', 'title'),
            },
        ),
    ]
