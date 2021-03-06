# Generated by Django 3.1.1 on 2021-02-08 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.CharField(max_length=30)),
                ('quantity', models.IntegerField()),
                ('expiry_date', models.DateField()),
                ('mrp', models.IntegerField()),
                ('lot_number', models.IntegerField()),
                ('transaction_id', models.CharField(max_length=30, unique=True)),
                ('transaction_type', models.IntegerField()),
                ('transaction_ts', models.DateTimeField()),
            ],
        ),
    ]
