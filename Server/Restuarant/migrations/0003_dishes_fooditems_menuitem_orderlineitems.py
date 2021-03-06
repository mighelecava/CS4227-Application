# Generated by Django 3.2.8 on 2021-11-06 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Restuarant', '0002_auto_20211102_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('menu_item', models.AutoField(primary_key=True, serialize=False)),
                ('Dish_Bev_id', models.IntegerField()),
                ('food', models.BooleanField()),
                ('menu_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='Restuarant.menu')),
            ],
        ),
        migrations.CreateModel(
            name='OrderLineItems',
            fields=[
                ('OrderLineItems', models.AutoField(primary_key=True, serialize=False)),
                ('food', models.BooleanField()),
                ('menu_item', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='Restuarant.menuitem')),
                ('order_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='Restuarant.orders')),
            ],
        ),
        migrations.CreateModel(
            name='Dishes_FoodItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='Restuarant.dishes')),
                ('food_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='Restuarant.fooditems')),
            ],
        ),
    ]
