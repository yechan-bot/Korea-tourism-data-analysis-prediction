# Generated by Django 3.2 on 2021-05-02 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('function_02', '0005_remove_resulttable_result2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
