# Generated by Django 2.0.5 on 2018-06-03 23:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library_app', '0005_auto_20180601_1721'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrowing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modification_date', models.DateTimeField(auto_now=True)),
                ('due_date', models.DateField()),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='library_app.Book')),
                ('borrower', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='borrower', to=settings.AUTH_USER_MODEL)),
                ('lender', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lender', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
