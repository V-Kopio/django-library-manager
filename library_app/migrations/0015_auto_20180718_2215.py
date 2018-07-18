# Generated by Django 2.0.6 on 2018-07-18 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0014_book_borrowings_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowing',
            name='borrower',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='borrower', to='library_app.LibraryUser'),
        ),
        migrations.AlterField(
            model_name='borrowing',
            name='lender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lender', to='library_app.LibraryUser'),
        ),
    ]
