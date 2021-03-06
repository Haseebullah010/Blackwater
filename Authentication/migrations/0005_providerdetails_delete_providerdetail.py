# Generated by Django 4.0.1 on 2022-01-21 05:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Authentication', '0004_auto_20220117_1709'),
    ]

    operations = [
        migrations.CreateModel(
            name='providerdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_detail', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('password2', models.CharField(max_length=30)),
                ('num', models.CharField(max_length=30)),
                ('security_num', models.CharField(max_length=30)),
                ('note', models.CharField(max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='providerdetail',
        ),
    ]
