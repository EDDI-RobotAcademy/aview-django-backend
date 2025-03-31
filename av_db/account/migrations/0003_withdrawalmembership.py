# Generated by Django 5.1.6 on 2025-03-31 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WithdrawalMembership',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('accountId', models.CharField(max_length=50)),
                ('withdraw_at', models.DateTimeField(null=True)),
                ('withdraw_end', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'withdrawal_membership',
            },
        ),
    ]
