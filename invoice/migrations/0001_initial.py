# Generated by Django 3.0.3 on 2020-02-18 11:21

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter Customer or Company', max_length=256)),
                ('address', models.CharField(blank=True, help_text='Enter address of customer or Company', max_length=100, null=True)),
                ('city', models.CharField(blank=True, help_text='Enter the city of the address', max_length=100, null=True)),
                ('region', models.CharField(blank=True, help_text='Enter the region of the address', max_length=50, null=True)),
                ('country', models.CharField(blank=True, help_text='Enter the country of the address', max_length=100, null=True)),
                ('email', models.EmailField(blank=True, help_text='Enter the email of the customer or Company', max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_code', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('valid', models.BooleanField(default=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('expiration_date', models.DateField()),
                ('status', models.CharField(max_length=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('qty', models.IntegerField()),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice.Invoice')),
            ],
        ),
    ]
