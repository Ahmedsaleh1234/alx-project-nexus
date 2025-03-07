# Generated by Django 5.1.6 on 2025-03-03 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_contact_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_decription', models.CharField(max_length=200)),
                ('product_image', models.ImageField(upload_to='product_images')),
            ],
        ),
    ]
