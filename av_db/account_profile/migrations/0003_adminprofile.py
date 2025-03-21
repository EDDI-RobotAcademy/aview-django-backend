# Generated by Django 5.1.4 on 2025-03-21 01:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0002_initial"),
        ("account_profile", "0002_alter_accountlogintype_logintype"),
    ]

    operations = [
        migrations.CreateModel(
            name="AdminProfile",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("email", models.CharField(max_length=32, unique=True)),
                (
                    "account",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="admin_profile",
                        to="account.account",
                    ),
                ),
            ],
            options={
                "db_table": "admin_profile",
            },
        ),
    ]
