# Generated by Django 4.1.6 on 2023-02-20 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genration_01',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10)),
                ('main_dp', models.ImageField(blank=True, upload_to='dp')),
                ('partner', models.CharField(blank=True, max_length=100, null=True)),
                ('partner_dp', models.ImageField(blank=True, upload_to='dp')),
                ('slug', models.SlugField(choices=[('appala-naidu', 'appalanaidu'), ('brother-2', 'brother2'), ('pothala-1', 'pothala1')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Genration_02',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_name', models.CharField(max_length=200, null=True)),
                ('name', models.CharField(max_length=100)),
                ('main_dp', models.ImageField(blank=True, upload_to='dp')),
                ('partner', models.CharField(blank=True, max_length=100, null=True)),
                ('partner_dp', models.ImageField(blank=True, upload_to='dp')),
                ('gen_code', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10)),
                ('whatsapp_no', models.BigIntegerField(blank=True, null=True)),
                ('phone_no', models.BigIntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('d_no', models.CharField(max_length=10, null=True)),
                ('street', models.CharField(max_length=40)),
                ('mandal', models.CharField(max_length=100)),
                ('pin_code', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('co_state', models.CharField(max_length=100)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.genration_01')),
            ],
        ),
    ]