# Generated by Django 5.1.4 on 2025-03-10 08:52

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("account", "0002_initial"),
        ("company_report", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Marketing",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("click_count", models.PositiveSmallIntegerField(default=1)),
                ("purchase", models.BooleanField(default=False)),
                (
                    "last_click_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="marketing",
                        to="account.account",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="marketing",
                        to="company_report.companyreport",
                    ),
                ),
            ],
            options={
                "db_table": "marketing",
            },
        ),
    ]
