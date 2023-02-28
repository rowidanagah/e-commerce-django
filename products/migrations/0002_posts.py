# Generated by Django 4.1.7 on 2023-02-28 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.CharField(blank=True, max_length=100, null=True)),
                ('version', models.IntegerField(default=1)),
                ('publisher_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('privacy', models.CharField(choices=[('1', 'Public'), ('2', 'Private')], max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
