# Generated by Django 3.2.2 on 2021-05-10 06:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='skills',
            field=models.ManyToManyField(to='matcher.Skill'),
        ),
    ]
