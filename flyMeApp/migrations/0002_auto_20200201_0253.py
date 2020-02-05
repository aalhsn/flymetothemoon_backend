# Generated by Django 3.0.2 on 2020-02-01 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flyMeApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booked_flights', to='flyMeApp.Ticket'),
        ),
    ]
