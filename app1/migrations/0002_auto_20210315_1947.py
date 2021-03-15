# Generated by Django 3.0.6 on 2021-03-15 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizzatops',
            name='amount',
        ),
        migrations.AddField(
            model_name='pizzatops',
            name='pizza_size',
            field=models.CharField(choices=[(1, 'small'), (2, 'medium'), (3, 'big')], default='n', max_length=1),
        ),
        migrations.CreateModel(
            name='PizzaOrderTops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('pizza_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.PizzaOrder')),
                ('pizza_top', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.PizzaTops')),
            ],
        ),
        migrations.AddField(
            model_name='pizzaorder',
            name='toppings',
            field=models.ManyToManyField(through='app1.PizzaOrderTops', to='app1.PizzaTops'),
        ),
    ]
