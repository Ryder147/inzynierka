# Generated by Django 4.0.6 on 2022-08-13 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoOP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='avBooked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateBooked', models.DateField()),
            ],
        ),
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='user_name',
        ),
        migrations.AddField(
            model_name='user',
            name='availability_end',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='availability_start',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='photo_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='user',
            name='avbooked',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DjangoOP.avbooked'),
        ),
    ]