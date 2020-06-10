# Generated by Django 3.0.6 on 2020-05-21 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200517_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('pic', models.FileField(upload_to='images/')),
                ('author', models.CharField(max_length=50)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
