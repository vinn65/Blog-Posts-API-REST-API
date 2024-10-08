# Generated by Django 3.2.2 on 2024-09-13 08:36

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='name', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images')),
                ('content', models.TextField()),
                ('blog_slug', autoslug.fields.AutoSlugField(default=True, editable=False, null=True, populate_from='title', unique=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('1', 'PUBLISH'), ('0', 'DRAFT')], default=0, max_length=1)),
                ('main_post', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='blogs.category')),
            ],
        ),
    ]
