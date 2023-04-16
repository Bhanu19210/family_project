# Generated by Django 4.1.6 on 2023-02-20 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_genration_01_genration_02'),
    ]

    operations = [
        migrations.AddField(
            model_name='genration_02',
            name='parent_slug',
            field=models.SlugField(choices=[('appala-naidu', 'appalanaidu'), ('brother-2', 'brother2'), ('pothala-1', 'pothala1')], default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='genration_02',
            name='slug',
            field=models.SlugField(default='', null=True),
        ),
    ]
