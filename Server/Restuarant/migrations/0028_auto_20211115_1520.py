# Generated by Django 3.2.9 on 2021-11-15 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restuarant', '0027_alter_employeesalary_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beverages',
            name='price',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='dishes',
            name='price',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='employeesalary',
            name='salary',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='menu',
            name='discount',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='menu',
            name='set_menu_price',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='orders',
            name='total_cost',
            field=models.CharField(max_length=50),
        ),
    ]