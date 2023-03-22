# Generated by Django 4.1.7 on 2023-03-22 03:02

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccountType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('maximum_withdrawal_amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('annual_interest_rate', models.DecimalField(decimal_places=2, help_text='Interest rate from 0 - 100', max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('interest_calculation_per_year', models.PositiveSmallIntegerField(help_text='The number of times interest will be calculated per year', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserBankAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_no', models.PositiveIntegerField(unique=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('interest_start_date', models.DateField(blank=True, help_text='The month number that interest calculation will start from', null=True)),
                ('initial_deposit_date', models.DateField(blank=True, null=True)),
                ('account_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='banking.bankaccounttype')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='account', to='banking.user')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('balance_after_transaction', models.DecimalField(decimal_places=2, max_digits=12)),
                ('transaction_type', models.PositiveSmallIntegerField(choices=[(1, 'Deposit'), (2, 'Withdrawal'), (3, 'Interest')])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='banking.userbankaccount')),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
    ]
