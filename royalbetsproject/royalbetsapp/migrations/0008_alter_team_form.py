# Generated by Django 4.0.6 on 2022-09-16 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('royalbetsapp', '0007_alter_team_form'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='form',
            field=models.CharField(blank=True, default='?????', max_length=5),
        ),
    ]
