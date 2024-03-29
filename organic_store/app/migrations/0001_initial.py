# Generated by Django 4.2.7 on 2023-12-11 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='additem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=20, unique=True)),
                ('product_name', models.CharField(max_length=10)),
                ('price', models.CharField(max_length=20)),
                ('stock', models.CharField(max_length=20)),
                ('image', models.FileField(upload_to='static')),
            ],
        ),
        migrations.CreateModel(
            name='regshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ownername', models.CharField(max_length=20)),
                ('shopname', models.CharField(max_length=20, unique=True)),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
                ('re_password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='reguser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yourname', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
                ('repassword', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.additem')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.reguser')),
            ],
        ),
        migrations.AddField(
            model_name='additem',
            name='shopname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.regshop'),
        ),
    ]
