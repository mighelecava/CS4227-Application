# Generated by Django 3.2.9 on 2021-11-08 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restuarant', '0005_loyalty_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beverages',
            fields=[
                ('beverage_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('price', models.DecimalField(decimal_places=10, max_digits=10)),
                ('alcoholic', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Dishes',
            fields=[
                ('dish_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('price', models.DecimalField(decimal_places=10, max_digits=10)),
                ('allergens', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('menu_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('date_created', models.DateField()),
                ('set_menu_price', models.DecimalField(decimal_places=10, max_digits=10)),
                ('discount', models.DecimalField(decimal_places=10, max_digits=10)),
                ('two_for_one', models.BooleanField()),
            ],
        ),
    ]
