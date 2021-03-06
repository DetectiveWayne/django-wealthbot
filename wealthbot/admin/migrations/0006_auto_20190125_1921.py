# Generated by Django 2.1.4 on 2019-01-25 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webo_admin', '0005_auto_20190125_1517'),
    ]

    operations = [
        migrations.CreateModel(
            name='Security',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('symbol', models.CharField(max_length=255, unique=True)),
                ('expense_ratio', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'securities',
            },
        ),
        migrations.CreateModel(
            name='SecurityAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_preferred', models.BooleanField()),
                ('muni_substitution', models.BooleanField()),
                ('model', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='webo_admin.CeModel')),
                ('security', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='securityAssignments', to='webo_admin.Security')),
                ('subclass', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='securityAssignments', to='webo_admin.Subclass')),
            ],
            options={
                'db_table': 'securities_assignments',
            },
        ),
        migrations.CreateModel(
            name='SecurityType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('description', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'security_types',
            },
        ),
        migrations.AddField(
            model_name='cemodelentity',
            name='nb_edits',
            field=models.SmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cemodelentity',
            name='percent',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='security',
            name='security_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webo_admin.SecurityType'),
        ),
        migrations.AddField(
            model_name='cemodelentity',
            name='security_assignment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='webo_admin.SecurityAssignment'),
            preserve_default=False,
        ),
    ]
