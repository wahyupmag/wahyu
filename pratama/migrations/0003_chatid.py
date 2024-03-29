# Generated by Django 4.2.6 on 2024-01-12 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pratama', '0002_alter_produk_gambar'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chatid', models.CharField(max_length=200, null=True)),
                ('nama', models.CharField(max_length=200, null=True)),
                ('aktif', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Data Chat ID',
            },
        ),
    ]
