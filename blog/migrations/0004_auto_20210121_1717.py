# Generated by Django 3.1.5 on 2021-01-21 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_category_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('created_at',), 'verbose_name_plural': 'Categories'},
        ),
    ]
