# Generated by Django 5.1.1 on 2024-11-25 21:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("productos", "0004_comment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="fk_producto",
                to="productos.producto",
            ),
        ),
    ]
