# Generated by Django 2.2.28 on 2023-06-07 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_mail', models.CharField(max_length=100)),
                ('reg_pwd', models.CharField(max_length=100)),
            ],
        ),
    ]
