# Generated by Django 3.2.7 on 2021-09-29 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_alter_orderrating_rating'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={},
        ),
        migrations.RemoveField(
            model_name='order',
            name='created',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_status',
        ),
        migrations.RemoveField(
            model_name='order',
            name='updated',
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='key', to='orders.order'),
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_status', models.CharField(choices=[('Order Placed', 'Order Placed'), ('Order Accepted', 'Order Accepted'), ('In Transit', 'In Transit'), ('Delivered', 'Delivered')], default='Order Placed', max_length=20)),
                ('order_created', models.DateTimeField(auto_now=True)),
                ('order_updated', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status_key', to='orders.order')),
            ],
            options={
                'ordering': ('-order_created',),
            },
        ),
    ]
