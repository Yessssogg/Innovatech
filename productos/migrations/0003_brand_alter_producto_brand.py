# Generated by Django 5.1.1 on 2024-10-08 23:18

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("productos", "0002_producto_last_update_alter_producto_discount"),
    ]

    operations = [
        migrations.CreateModel(
            name="Brand",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "created_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("published_date", models.DateTimeField(blank=True, null=True)),
                ("last_update", models.DateTimeField(blank=True, null=True)),
                (
                    "logo",
                    models.ImageField(
                        blank=True, null=True, upload_to="media/productos"
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="producto",
            name="brand",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="fk_brand",
                to="productos.brand",
            ),
        ),
    ]