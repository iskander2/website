# Generated by Django 3.2.9 on 2021-12-15 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
        ('profiles', '0002_comement'),
    ]

    operations = [
        migrations.AddField(
            model_name='comement',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='app.product'),
            preserve_default=False,
        ),
    ]
