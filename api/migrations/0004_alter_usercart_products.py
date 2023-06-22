# Generated by Django 4.1.9 on 2023-06-22 10:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0003_alter_product_options_alter_product_table_usercart_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usercart",
            name="products",
            field=models.ManyToManyField(
                related_name="user_cart_products", to="api.product"
            ),
        ),
    ]
