# Generated by Django 4.2.8 on 2024-01-02 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='cast',
            new_name='cast1',
        ),
        migrations.AddField(
            model_name='movie',
            name='cast2',
            field=models.CharField(default=1234, max_length=150),
            preserve_default=False,
        ),
    ]
