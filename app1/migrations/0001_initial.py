# Generated by Django 3.0.6 on 2021-03-06 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=255)),
                ('postal_code', models.CharField(max_length=12, verbose_name='Postal code')),
                ('city', models.CharField(max_length=255, verbose_name='City')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('note', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('size', models.IntegerField(choices=[(1, 'small'), (2, 'medium'), (3, 'big')])),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=50)),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='app1.Address')),
            ],
        ),
        migrations.CreateModel(
            name='PizzaTops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(choices=[('h', 'half'), ('n', 'normal'), ('d', 'double')], default='n', max_length=1)),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Pizza')),
                ('topping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Topping')),
            ],
        ),
        migrations.CreateModel(
            name='PizzaOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Order')),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Pizza')),
            ],
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings',
            field=models.ManyToManyField(through='app1.PizzaTops', to='app1.Topping'),
        ),
        migrations.AddField(
            model_name='order',
            name='pizza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='app1.Pizza'),
        ),
        migrations.AddField(
            model_name='order',
            name='pizzas',
            field=models.ManyToManyField(through='app1.PizzaOrder', to='app1.Pizza'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.User'),
        ),
    ]