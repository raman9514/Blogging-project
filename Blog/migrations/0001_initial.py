# Generated by Django 3.0.7 on 2020-08-16 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('category', models.CharField(max_length=60)),
                ('desc', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, upload_to='posts/%Y/%m/%d')),
            ],
        ),
    ]