# Generated by Django 4.1.1 on 2022-09-28 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Clothes', 'Clothes'), ('Technology', 'Technology'), ('Furniture', 'Furniture'), ('No Category', 'No Category')], max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='saller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=50)),
                ('profile', models.TextField(blank=True, max_length=200)),
                ('photo', models.ImageField(default='image.png', upload_to='saller/images')),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=2000)),
                ('price', models.IntegerField()),
                ('photo', models.ImageField(default='image.png', upload_to='product/images')),
                ('saller', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Product_Saller', to='products.saller')),
            ],
        ),
    ]
