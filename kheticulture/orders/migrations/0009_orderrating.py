# Generated by Django 3.2.7 on 2021-09-06 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_alter_order_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderRating',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rating', models.IntegerField(blank=True)),
                ('review', models.TextField(blank=True, help_text='Not Required', verbose_name='description')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
        ),
    ]