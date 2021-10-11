# Generated by Django 3.2.8 on 2021-10-10 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, null=True)),
                ('phone_number', models.IntegerField(null=True)),
                ('image', models.ImageField(null=True, upload_to='upload/')),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
    ]
