# Generated by Django 5.1.6 on 2025-03-06 11:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('needy', '0008_alter_needy_street'),
    ]

    operations = [
        migrations.AddField(
            model_name='needy',
            name='house_number',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='پلاک'),
        ),
        migrations.AlterField(
            model_name='street',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='نام خیابان'),
        ),
        migrations.CreateModel(
            name='NeedyPath',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='نام مسیر')),
                ('street', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='paths', to='needy.street', verbose_name='خیابان مربوطه')),
            ],
        ),
    ]
