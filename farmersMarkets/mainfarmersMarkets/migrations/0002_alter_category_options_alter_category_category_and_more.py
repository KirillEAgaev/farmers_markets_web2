# Generated by Django 5.0.6 on 2024-06-10 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainfarmersMarkets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Категории продуктов'},
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=50, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='city',
            name='city',
            field=models.CharField(max_length=100, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='market',
            name='market_name',
            field=models.CharField(max_length=100, verbose_name='Название рынка'),
        ),
        migrations.AlterField(
            model_name='market',
            name='street',
            field=models.CharField(max_length=100, verbose_name='Улица'),
        ),
        migrations.AlterField(
            model_name='state',
            name='state_abbr',
            field=models.CharField(max_length=2, verbose_name='Аббревиатура штата'),
        ),
        migrations.AlterField(
            model_name='state',
            name='state_full',
            field=models.CharField(max_length=100, verbose_name='Штат'),
        ),
        migrations.AlterField(
            model_name='user',
            name='fname',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='lname',
            field=models.CharField(max_length=100, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password_hash',
            field=models.CharField(max_length=100, verbose_name='Пароль'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=100, verbose_name='Имя пользователя'),
        ),
    ]
