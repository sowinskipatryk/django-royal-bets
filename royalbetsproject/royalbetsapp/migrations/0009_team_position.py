# Generated by Django 4.0.6 on 2022-09-16 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('royalbetsapp', '0008_alter_team_form'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='position',
            field=models.IntegerField(default=0),
        ),
    ]
