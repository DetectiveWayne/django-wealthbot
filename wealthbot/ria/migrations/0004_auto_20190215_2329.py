# Generated by Django 2.1.4 on 2019-02-15 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webo_admin', '0011_securitytransaction'),
        ('ria', '0003_auto_20190112_0955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='riacompanyinformation',
            name='portfolio_model_id',
        ),
        migrations.AddField(
            model_name='riacompanyinformation',
            name='portfolio_model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='webo_admin.CeModel'),
        ),
        migrations.AlterField(
            model_name='riacompanyinformation',
            name='account_managed',
            field=models.IntegerField(blank=True, choices=[(1, 'Account Level'), (2, 'Household Level'), (3, 'Account or Household Level')], null=True),
        ),
        migrations.AlterField(
            model_name='riacompanyinformation',
            name='portfolio_processing',
            field=models.IntegerField(blank=True, choices=[(1, 'Straight-Through'), (2, 'Collaborative')], null=True),
        ),
    ]
