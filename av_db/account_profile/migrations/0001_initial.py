# Generated by Django 5.1.4 on 2025-03-04 06:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AccountLoginType",
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
                (
                    "loginType",
                    models.CharField(
                        choices=[
                            ("KAKAO", "Kakao"),
                            ("GOOGLE", "google"),
                            ("NAVER", "naver"),
                        ],
                        max_length=10,
                    ),
                ),
            ],
            options={
                "db_table": "account_login_type",
            },
        ),
        migrations.CreateModel(
            name="AccountProfile",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("profile_nickname", models.CharField(max_length=32, unique=True)),
                ("account_email", models.CharField(max_length=32, unique=True)),
                ("gender", models.CharField(max_length=32, unique=True)),
                ("age_range", models.IntegerField()),
                ("birthyear", models.IntegerField()),
                (
                    "loginType",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="account_profile.accountlogintype",
                    ),
                ),
            ],
            options={
                "db_table": "account_profile",
            },
        ),
    ]
