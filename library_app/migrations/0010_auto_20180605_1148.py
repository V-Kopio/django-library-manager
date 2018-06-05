# Generated by Django 2.0.6 on 2018-06-05 11:48

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('library_app', '0009_auto_20180604_2222'),
    ]

    operations = [
        migrations.CreateModel(
            name='LibraryUser',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='borrowing',
            name='borrower',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='borrower', to='library_app.LibraryUser'),
        ),
        migrations.AlterField(
            model_name='borrowing',
            name='lender',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lender', to='library_app.LibraryUser'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='reserver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reserver', to='library_app.LibraryUser'),
        ),
    ]
